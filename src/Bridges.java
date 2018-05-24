package bridges.connect;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

import bridges.base.*;
import bridges.data_src_dependent.*;
import bridges.validation.*;


/**
 * 	@brief The Bridges class is the main class that provides interfaces to datasets,
 *	maintains user and assignment information, and connects to the Bridges server.
 *
 * 	The Bridges class is responsible  for initializing the Bridges system, specifying
 * 	parameters (user id, assignment id, title, description, data structure
 *	type, etc) for the student assignment, generating the data structure representation
 *	and transmission to the Bridges server. In addition, it provides interfaces to
 *	a number of real-world datasets, that makes it easy to access the data for use
 * 	algorithms/data structure assignments. <br>
 *
 *  <b>Datasets.</b> The datasets that are currently supported through the BRIDGES API
 *	include USGS Earthquake Data, IMDB Actor/Movie Data (2 versions), Gutenberg Book
 *	Collection Meta Data, a Video Game Dataset and Shakespeare Dataset. More information
 *	is found in the respective methods (below) and at <p>
 *	http://bridgesuncc.github.io/datasets.html <p>
 *
 *	A typical Bridges program includes creating the Bridges object, followed by creation
 *  of the data structure by the user, assigning visual attributes to elements of the
 *	data structure, followed by specification of teh data structure type  and the
 *	call to visualize the data structure (Bridges::setDataStructure() and visualize()
 *	methods).
 *
 * 	@author Sean Gallagher, Kalpathi Subramanaian, Mihai Mehedint, David Burlinson.
 *
 * 	@date  1/16/17, 5/19/17
 *
 *	\sa Tutorial examples at <br>
 *	http://bridgesuncc.github.io/Hello_World_Tutorials/Overview.html
 */

public class Bridges {

	private static int assignmentDecimal = 0;
	//	protected ADTVisualizer<K, E> visualizer;
	private  Connector connector;
	//	private Element<E> root;
	//	private GraphAdjList<K, E>  graph_adj_list;
	//	private GraphAdjMatrix<K, E>  graph_adj_matrix;
	//	private Element<E>[]  element_array;
	//	private Array<E>  br_array;
	private int element_array_size;
	private static boolean json_flag = false;
	private static int assignment;
	private static int assignment_part;
	private static String key;
	private static DataFormatter df;
	private static String userName, vis_type,
			title, description;
	private static Integer MaxTitleSize = 50,
						   MaxDescrSize = 1000;
	private static String[] projection_options = {"Cartesian", "albersUsa", "equirectangular"};

	private static Boolean map_overlay = false;	// default to no map overlay
	private static String coord_system_type = projection_options[0];	// default to Cartesian space

	private static DataStruct ds_handle = null;		// data structure handle

	//  string constants  for use in constructing JSON
	//  representation of the data structure

	private static String
	QUOTE = "\"",
	COMMA = ",",
	COLON = ":",
	OPEN_CURLY = "{",
	CLOSE_CURLY = "}",
	OPEN_PAREN = "(",
	CLOSE_PAREN = ")",
	OPEN_BOX = "[",
	CLOSE_BOX = "]";
	/**
	 *
	 *	Constructors
	 *
	 */
	public Bridges() {
		super();
		connector = new Connector();
		df = new DataFormatter();
		assignment_part = 0;
		title = new String();
		description = new String();
	}

	/**
	 * Initialize Bridges (Constructor)
	 *
	 * @param assignment this is the assignmen id (integer)
	 * @param appl_id    this is the appl authentication key(from the Bridges account)
	 * @param username   this is the username (from the Bridges account)
	 *
	 */
	public Bridges(int assignment, String appl_id, String username) {
		this();
		init(assignment, appl_id, username);
	}

	/**
	 *
	 * Initialize Bridges
	 *
	 * @param <E>
	 * @param assignment this is the assignmen id (integer)
	 * @param appl_id    this is the appl authentication key(from the Bridges account)
	 * @param username   this is the username (from the Bridges account)
	 *
	 */
	public void init(int assignment, String appl_id, String username) {
		Bridges.setAssignment(assignment);
		Bridges.key = appl_id;
		Bridges.userName = username;
	}


	/**
	 *
	 *	Bridges JSON Parameters
	 *
	 */

	/**
	 *
	 * @param title title used in the visualization;
	 *
	 */
	public void setTitle(String title) {
		if (title.length() > MaxTitleSize) {
			System.out.println ("Visualization Title restricted to " + MaxTitleSize + " characters."
				+ " Truncating title..");
			this.title = title.substring(0, MaxTitleSize);
		}
		else
			this.title = title;
	}

	/**
	 *
	 * @param descr description to annotate the visualization;
	 *
	 */
	public void setDescription(String description) {
		if (description.length() > MaxDescrSize) {
			System.out.println ("Visualization Description restricted to " + MaxDescrSize + " characters."
				+ " Truncating description..");
			this.description = description.substring(0, MaxDescrSize);
		}
		else
			this.description = description;
	}

	/**
	 *
	 * 	@param  server server to which to connect.
	 *		Options are: ['live', 'local', 'clone'], and 'live' is the default;
	 *
	 */
	public void setServer(String server) {
		connector.setServer(server);
	}

	/**
	 * 	@param flag 	this is the boolean flag for displaying a map overlay
	 **/
	public void setMapOverlay (Boolean flag) {
		map_overlay = flag;
	}

	/**
	 * 	@param coord 	this is the desired coordinate space argument
	 *		Options are: ['Cartesian', 'albersUsa', 'equirectangular'], and 'Cartesian' is the default;
	 **/
	public void setCoordSystemType (String coord) {
		if (java.util.Arrays.asList(projection_options).indexOf(coord) >= 0) {
			coord_system_type = coord;
		}
		else  {
			System.err.println("Unrecognized coordinate system \'" + coord + "\', defaulting to Cartesian. Options:");
			for (String prj : projection_options) {
				System.err.print(prj + "\t");
			}
			coord_system_type = "Cartesian";
		}
	}

	/**
	 * 	@param check if the flag to output the JSON is set
	**/
	public boolean visualizeJSON() {
		return json_flag;
	}

	/**
	 * 	@param set the flag to print the JSON represenation of the data structure
	 *		to standard output
	 **/
	public void setVisualizeJSON (boolean flag) {
		json_flag = flag;
	}

	/**
	 *  This helper function provides a simple API to retrieve current USGS earthquake
	 *	Tweet data from the USGS website (https://earthquake.usgs.gov/earthquakes/map/);
	 *  The data is retrieved and formatted into a list of EarthquakeUSGS objects.
	 *
	 *  More information on the dataset can be found at <p>
	 *  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://bridgesuncc.github.io/datasets.html <p>
	 *
	 *  @param name   USGS account name - must be "earthquake" to create account
	 *	@param maxElements  the number of earthquake records retrieved, limited to 5000
	 *  @throws Exception if the request fails
	 *
	 *  @return a list of earthquake records
	 */
	public static List<EarthquakeUSGS> getEarthquakeUSGSData(USGSaccount name,
		int maxElements) throws Exception {
		return DataFormatter.getEarthquakeUSGSData(name, maxElements);
	}

	/**
	 *  This helper function provides access to a small curated IMDB dataset. The data is
	 *  retrieved, formatted into a list of ActorMovieIMDB objects (about 1800 pairs).
	 *
	 *  This curated data set has only actor and movie name pairs. refer to <p>
	 *  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://bridgesuncc.github.io/datasets.html <p>
	 *  for more information and to look at the dataset.
	 *
	 *  @param name   should be "IMDB"
	 *  @param maxElements  the number of actor/movie pairs(but currently unused),
	 *	 							returns all records.
	 *  @throws Exception if the request fails
	 *
	 *  @return a list of ActorMovieIMDB objects, but only actor,  movie, movie genre
	 *			and movie rating are returned.
	 */
	public static List<ActorMovieIMDB> getActorMovieIMDBData(String name,
		int maxElements) throws Exception {
		return DataFormatter.getActorMovieIMDBData(name, maxElements);
	}
	/**
	 *  This helper function provides access to a second curated IMDB dataset; the data is
	 *  retrieved, formatted into a list of ActorMovieIMDB objects
	 *
	 *  This version of the IMDB Actor/Movie data contains for each record,
	 *	actor name, movie name, movie genres, movie rating; refer to <p>
	 *	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://bridgesuncc.github.io/datasets.html <p>
	 *  for more information and to look at the dataset.
	 *
	 *  @param name   should be "IMDB"
	 *  @param maxElements  the number of actor/movie pairs, but currently unused,
	 *	 	returns all records.
	 *  @throws Exception if the request fails
	 *
	 *  @return a list of ActorMovieIMDB objects
	 */
	public static List<ActorMovieIMDB> getActorMovieIMDBData2() throws Exception {
		return DataFormatter.getActorMovieIMDBData2();
	}
	/**
	 *  This helper function provides access to the meta-data of the Gutenberg book
	 *	collection (about 1000 books); the data is retrieved, formatted into a
	 *	list of GutenbergBook objects.
	 *
	 *  Each book in this collection has  for each record,
	 *	information on author (name, birth, death), title, languages, genres,
	 *  subjects, metrics(number of chars, words, sentences, difficult words), url
	 *	downloads. More information and commands to access the data can be found at <p>
	 *	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://bridgesuncc.github.io/datasets.html <br>
	 *  for more information and to look at the dataset.
	 *
	 *  @throws Exception if the request fails
	 *
	 *  @return a list of GutenbergBook objects
	 */
	public static List<GutenbergBook> getGutenbergBookMetaData() throws Exception {
		return DataFormatter.getGutenbergBookMetaData();
	}
	/**
	 *  This helper function provides access to the meta-data of the video game
	 *	collection.
	 *
	 *  Each record in this collection has
	 *	information on game title, platform, rating, and genre. For more information
	 *	and to look at the data, refer to <p>
	 *	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://bridgesuncc.github.io/datasets.html <p>
	 *
	 *  @throws Exception if the request fails
	 *
	 *  @return a list of Game objects.
	 */
	public static List<Game> getGameData() throws Exception {
		return DataFormatter.getGameData();
	}

	/**
	 *  This helper function provides access to a collection of Shakespeare plays,
	 * 	poems and plays.
	 *
	 *  Each record in this collection has
	 *	information on title, type (poem, Sonnet, play) and text. <br>
	 *
	 *	For more information and to look at the data, refer to <p>
	 *	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://bridgesuncc.github.io/datasets.html <p>
	 *
	 *  @throws Exception if the request fails
	 *
	 *  @return a list of Shakespeare objects.
	 */
	public static List<Shakespeare> getShakespeareData() throws Exception {
		return DataFormatter.getShakespeareData();
	}

	/**
	 *  This helper function provides access to a cancer dataset from CDC
	 *  https://www.cdc.gov/cancer/npcr/uscs/download_data.htm and curated
	 *  by Austin (Cory) Bart as part of the Corgis data collection
	 *	https://think.cs.vt.edu/corgis/
	 *
	 *  Each record in this collection has a number of fields detailed in the
	 *	CancerIncidence class.
	 *
	 *	For more information and to look at the data, refer to <p>
	 *	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://bridgesuncc.github.io/datasets.html <p>
	 *
	 *  @throws Exception if the request fails
	 *
	 *  @return a list of Cancer incidence objects.
	 */
	public static ArrayList<CancerIncidence> getCancerIncidenceData() throws Exception {
		return DataFormatter.getCancerIncidenceData();
	}

	/**
	 *	Get the assignment id
	 *
	 *  @return assignment as a string
	 *
	 */
	public static String getAssignment() {
		return (assignment_part < 10)
			? String.valueOf(assignment) + ".0" +
			String.valueOf(assignment_part)
			: String.valueOf(assignment) + "." +
			String.valueOf(assignment_part);
	}

	/**
	 *	set the assignment id
	 *
	 * @param assignment number (int)
	 *
	 **/
	public static void setAssignment(int assignment) {
		if (assignment  <  0)
			throw new IllegalArgumentException(
				"\n Assignment value must be >=  0.\n");
		else if (Bridges.assignment >= 0)
			Bridges.assignment_part = 0;

		Bridges.assignment = assignment;
	}

	/**
	 *
	 *	This exists to prevent duplicate error traces.
	 *
	 *	@return user id (string)
	 */
	public static String getUserName() {
		return userName;
	}

	/**
	 *	set User id
	 *
	 *	@param userName (string)
	 *
	 */
	public static void setUserName(String userName) {
		Bridges.userName = userName;
	}

	/**
	 *
	 *	Get application key
	 *
	 *	@return application key value (string)
	 *
	 */
	public static String getKey() {
		return key;
	}

	/**
	 *
	 *	Set application key
	 *
	 *	@param  key application key value (string)
	 *
	 */
	public static void setKey(String key) {
		Bridges.key = key;
	}

	/**
	 *
	 * 	This method sets  the handle to the current data structure; this can
	 *	be an array, the head of a linked list, root of a tree structure, a graph
	 *	Arrays of upto 3 dimensions are suppported. It can be any of the data
	 *	structures supported by BRIDGES. Polymorphism and type casting is used
	 *	to determine the actual data structure and extract its representtion.
	 *
	 * @param ds   The data structure to set (any of the subclasses of DataStruct)
	 *
	 */
	public void setDataStructure(DataStruct ds) throws NullPointerException {
		try {
			ds_handle = ds;
			vis_type =   ds.getDataStructType();
		}
		catch (NullPointerException e) {
			System.out.println("Exception Thrown: Data structure passed to BRIDGES is null!\n" + e);
			return ;
		}
	}

	/**
	 *
	 * This method generates the representation of the current data structure (JSON)
	 * and sends that to the Bridges server for generating a visualization.
	 *
	 * @throws RateLimitException
	 * @throws IOException
	 */
	public void visualize()  throws IOException, RateLimitException {
		String[] nodes_links = new String[2];
		String nodes_links_str = "";
		switch (vis_type) {
			case "Array":
				nodes_links_str = ((Array) ds_handle).getDataStructureRepresentation();
				break;
			case "SinglyLinkedList":
			case "DoublyLinkedList":
			case "CircularSinglyLinkedList":
			case "CircularDoublyLinkedList":
				nodes_links_str =
					((SLelement) ds_handle).getDataStructureRepresentation();
				break;
			case "MultiList":
				nodes_links_str =
					((MLelement) ds_handle).getDataStructureRepresentation();
				break;
			case "Tree":
			case "BinaryTree":
			case "BinarySearchTree":
			case "AVLTree":
				nodes_links_str =
					((TreeElement) ds_handle).getDataStructureRepresentation();
				break;
			case "GraphAdjacencyList":
				nodes_links_str =
					((GraphAdjList) ds_handle).getDataStructureRepresentation();
				break;
			case "GraphAdjacencyMatrix":
				nodes_links_str =
					((GraphAdjMatrix) ds_handle).getDataStructureRepresentation();
				break;
		}

		String ds_json =
			OPEN_CURLY +
			QUOTE + "visual"  + QUOTE + COLON + QUOTE + vis_type + QUOTE + COMMA +
			QUOTE + "title"   + QUOTE + COLON + QUOTE + title + QUOTE + COMMA +
			QUOTE + "description" + QUOTE + COLON + QUOTE + description + QUOTE + COMMA +
			QUOTE + "coord_system_type" + QUOTE + COLON + QUOTE + coord_system_type + QUOTE + COMMA +
			QUOTE + "map_overlay" + QUOTE + COLON + map_overlay + COMMA;

		// get the nodes and link representations

		if (vis_type == "Array") {
			int dims[] = new int[3];
			Array ds_array = (Array) ds_handle;
			int num_dims = ds_array.getNumDimensions();
			ds_array.getDimensions(dims);
			ds_json += QUOTE + "dims" + QUOTE + COLON +
				OPEN_BOX + dims[0] + COMMA + dims[1] + COMMA + dims[2] + CLOSE_BOX + COMMA;

			ds_json +=  nodes_links_str;

		}
		else {
			ds_json += nodes_links_str;
		}

		if (json_flag)		// print the JSON (mostly for debugging)
			System.out.println("\nJSON String:\n" + ds_json);

		// send the data structure to the server and visualize
		try {
			connector.post("/assignments/" + getAssignment(), ds_json);
		}
		catch (IOException e) {
			System.err.println("There was a problem sending the visualization"
				+ " representation to the server. \n"
				+ e.getMessage());
		}
		catch (RateLimitException e) {
			System.err.println("There was a problem sending the visualization"
				+ " representation to the server. However, it responded with"
				+ " an impossible 'RateLimitException'. "
				+ e.getMessage());
		}
		// Return a URL to the user
		System.out.println("\nCheck Your Visualization at the following link:\n\n" +
			connector.getServerURL() + "/assignments/" + assignment + "/"
			+ userName + "\n\n");
	}
}
