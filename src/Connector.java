package bridges.connect;

import java.io.IOException;
import java.util.Map;
import java.util.Map.Entry;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpResponseException;
import org.apache.http.client.fluent.*;
import org.apache.http.entity.ContentType;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.impl.client.LaxRedirectStrategy;
import org.apache.http.util.EntityUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import bridges.validation.RateLimitException;


public class Connector {
	String server_live = "http://bridges-cs.herokuapp.com";
	String server_clone = "http://bridges-clone.herokuapp.com";
	String server_local = "http://127.0.0.1:3000";

	String server_type = "application";
	String server_url = "http://bridges-cs.herokuapp.com";
	String usgs_url = "https://earthquakes-uncc.herokuapp.com/eq";  //usgs earthquakes url
	String airline_url = "https://earthquakes-uncc.herokuapp.com/airline"; //corgis airline data

	Executor http_connection;
	boolean debug = false;
	int pattern_found = 0; //semaphor
	protected Connector() {

		http_connection = Executor.newInstance(
				HttpClientBuilder
				.create()
				.setRedirectStrategy(new LaxRedirectStrategy())
				.build()
			);
		//    	System.out.println("hello from connector"+http_connection);
	}

	/* Accessors and Mutators */
	/**
	 * Set the current DataFormatters server to live, clone, or local, or throw an error;
	 * @param server
	 */
	public void setServer(String server) throws IllegalArgumentException {
		switch(server) {
				case "live":
					setServerURL(server_live);
					break;
				case "clone":
					setServerURL(server_clone);
					break;
				case "local":
					setServerURL(server_local);
					break;
				default:
					throw new IllegalArgumentException("Invalid server option. Please use one of the following options: ['live', 'clone', 'local'].");
		}
	}

	/**
	 * Get the current  base URL for the DataFormatters server (with no ending/)
	 * @return
	 */
	public String getServerURL() {
		//System.out.println("url:" + server_url);
		return server_url;
	}

	/**
	 * Set the current base URL for the DataFormatters server (with no ending /)
	 * @param server_url
	 */
	public void setServerURL(String server_url) {
		while (server_url.endsWith("/"))
			server_url = server_url.substring(0, server_url.length() - 1);
		if (server_url.length() > 0)
			this.server_url = server_url;
	}

	/**
	 * This reformats the coordinates in Earthwuake tweet such that there will be
	 * no arrays present when casting to the JSONObject. for  the resons described below
	 * Mihai
	 * @param text
	 * @return
	 */
	public String latlongFormatter (String text) {

		Pattern patt2 = Pattern.compile("(-?([0-9]*\\.?[0-9]+))");
		//-?([0-9]*\.?[0-9]+)
		//		System.out.println("Char seq text: "+text);
		//StringBuilder c = new StringBuilder();
		String c = "{\"latitude\":";
		//StringBuffer cBuffer = new StringBuffer(text.length());
		Matcher n = patt2.matcher(text);
		//n.find();
		//System.out.println("Whole coord: "+text+" group1 "+n.group(1));

		//StringBuffer coordBuffer = new StringBuffer(text.length());
		n.find();
		String coord = new String(n.group(1));
		c += coord + ",\"longitude\":";
		//System.out.println("group 1: "+ c);
		n.find();
		String coord2 = new String(n.group(1));
		c += coord2 + ",\"depth\":";
		//System.out.println("group 2: "+ c);
		n.find();
		String coord3 = new String(n.group(1));
		c += coord3 + "}";
		//		    System.out.println("group 3 "+ c);

		//m.appendReplacement(coordBuffer, Matcher.quoteReplacement(coord));
		//		    System.out.println("Formatted coordinates: "+coord);

		//m.appendTail(coordBuffer);

		return c.toString();

	}



	/**
	 * Find the pattern of the coordinates (as an array) and replace them with {"lat": value, "long":value}
	 * This is done since it is difficult to cast an JSONArray to a JSON object containing arrays
	 * Mihai
	 * @param text
	 * @return
	 */
	private String latlongFinder(String text) {

		//\\[-?[0-9]*\\.[0-9]*,-?[0-9]*\\.[0-9]*,-?[0-9]*\\.[0-9]*\\]
		Pattern patt = Pattern.compile("\\[-?[0-9]*.[0-9]*,.?-?[0-9]*.[0-9]*,.?-?[0-9]*.[0-9]*\\]");
		Matcher m = patt.matcher(text);

		//while (pattern_found!=1){
		StringBuffer coordBuffer = new StringBuffer(text.length());
		pattern_found = 1;
		int counter = 0;

		while (m.find()) {
			counter++;
			pattern_found = 0;
			String coord = m.group(0);
			//System.out.println("Groups first loop 0: "+m.group(0) + " 1: "+m.group(1));
			String repl = latlongFormatter(coord);

			//		   System.out.println("Found coordinates: "+coord + " counter: "+counter);
			//m.appendReplacement(coordBuffer, Matcher.quoteReplacement("{\"latitude\":115.4466,\"longitude\":37.8432,\"depth\":0.6}"));
			m.appendReplacement(coordBuffer, Matcher.quoteReplacement(repl));
			//coordBuffer.append(Matcher.quoteReplacement(repl));
		}
		m.appendTail(coordBuffer);
		//}
		//		  System.out.println("The coord buffer:"+coordBuffer.toString());

		return coordBuffer.toString();

	}
	/**
	 * Trimm the end of the earthquake data:     ,"products":{"String":[]}
	 *
	 * Important: future implementations could combine the above in one single
	 * method with a hash table for different patters
	 * Mihai
	 * @param text
	 * @return
	 */
	public String trimmLast(String text) {
		Pattern patt = Pattern.compile("\\{\"String\":(\\[.*\\]\\})");
		Matcher m = patt.matcher(text);
		StringBuffer coordBuffer = new StringBuffer(text.length());
		while (m.find()) {
			String coord = m.group(0);
			//		   System.out.println("Found coordinates: "+coord);
			m.appendReplacement(coordBuffer, Matcher.quoteReplacement("{}"));
		}
		m.appendTail(coordBuffer);
		return coordBuffer.toString();
	}

	/* JSON management */

	/**
	 * Decode a String containing JSON into a JSON Object, or throw an error.
	 * @param text  The input JSON text
	 * @return  A non-null JSON object
	 */
	public JSONObject asJSONObject(String text) throws IOException {
		JSONObject jo;
		//pattern_found=true;

		//while (pattern_found==0){
		//if (textlatlongFinder(text))
		String a = latlongFinder(text);
		text = a;
		String c = latlongFinder(a);
		//text = c;
		//System.out.println("c is: " +text);
		//}
		//pattern_found=0;

		//changing the coordinates format
		//System.out.println(a);
		//text = a;
		//String b=trimmLast(a);//trimming the end of Earthquake
		//text =b;
		// System.out.println(text);
		try {
			//    		System.out.println("line 157 connector asJsonObject after http request check JSONobject: "+ JSONValue.parse(text));

			//JSONParser parser = new JSONParser();

			//Object obj  = parser.parse(text);
			//System.out.println("Connector line 80 asJSON object parser.parse text: "+obj);
			//JSONArray array = new JSONArray();
			//array.add(obj);
			//System.out.println(array);
			jo = (JSONObject) JSONValue.parse(text);

		}
		catch (ClassCastException e) {
			throw new IOException("Received a malformed JSON response from the"
				+ " server (expecting a JSON object): " + text);
		}
		if (jo == null) {
			throw new IOException("Received an empty JSON response from the"
				+ " server. ");
		}
		if (jo.containsKey("error")) {
			throw new IOException("Server reported an error while serving"
				+ " request: " + jo.get("error"));
		}
		return jo;
	}

	/**
	 * Decode a String containing JSON into a JSON Array, or throw an error.
	 * @param text  The JSON Array as a string
	 * @return a non-null JSONArray
	 */
	public JSONArray asJSONArray(String text) throws IOException {
		JSONArray ja;
		try {
			ja = (JSONArray) JSONValue.parse(text);
		}
		catch (ClassCastException e) {
			// We didn't get an array.
			// If it is an object-with-error, then asJSON will error:
			asJSONObject(text);
			// asJSON didn't error so we just received the wrong type.
			throw new IOException("Received a malformed JSON response from the"
				+ " server. We were expecting a JSON array, but received"
				+ " a JSON object: " + text);
		}
		if (ja == null) {
			throw new IOException("Received an empty JSON response from the"
				+ " server: " + text);
		}
		return ja;
	}

	/**
	 * Form and throw a helpful error report as part of JSON traversal.
	 * @param sequence   The traversal we wanted to make
	 * @param cursor     Index into `sequence`, how far in the traversal we are
	 * @param any_json   Any JSON object
	 * @param report     Statement of what went wrong.
	 * @throws IOException
	 */
	private void safeJSONTraverseErrorReport(
		String sequence,
		int cursor,
		Object original_obj,
		String report
	) throws IOException {
		// This is not an array. Try to spit out a helpful error message.
		System.err.println("Received a malformed JSON response. An "
			+ "IOException follows. The error was near here: ");
		System.err.println(sequence);
		for (int i = 0; i < cursor; i++)
			System.err.print(" ");
		System.err.println("^");
		System.err.println("It occured while processing the following JSON:");
		System.err.println(original_obj);
		throw new IOException(report);
	}

	/**
	 * Traverse JSON in a type-safe manner.
	 * This is somewhat complicated, but comes with the advantage that the
	 * debugging reports are far clearer when you know the whole path you are
	 * searching for.
	 *
	 * Use this syntax:
	 * [ number ] to access an array element,
	 * ["quoted string"] to get an object attribute
	 *
	 * @param sequence
	 * @param o
	 */
	public Object safeJSONTraverse(
		String sequence,
		Object original,
		Class<?> target) throws IOException {
		// Make sure the syntax is right
		if (!sequence.matches("(\\[(\\d+|'[^']+')\\])*")) {
			throw new IOException("Could not understand JSON traversal \""
				+ sequence + "\". Please file a bug report with this"
				+ " error to the DataFormatters developers.");
		}
		// Make sure the input is not null
		if (original == null)
			safeJSONTraverseErrorReport(sequence, 0, original,
				"Input JSON is null.");

		// The cursor is where we are in `sequence`
		int cursor = 0;
		// This holds the object we will be running the next operation on.
		Object any_json = original;
		//    	System.out.println("Connector safeJSONTraverse line 188 any_JSON: "+any_json);
		// Parse `sequence`
		Pattern array_index_p = Pattern.compile("\\[(\\d+)\\]");
		Matcher array_index_m = array_index_p.matcher(sequence.substring(cursor));
		Pattern object_p = Pattern.compile("\\['([^']+)'\\]");
		Matcher object_m = object_p.matcher(sequence.substring(cursor));

		// startsWith()..
		while (cursor < sequence.length()) {
			if (array_index_m.find() && array_index_m.start() == 0) {
				// Get an array index
				int index = Integer.parseInt(array_index_m.group(1));
				JSONArray ja = null;
				try {
					ja = (JSONArray) any_json;
				}
				catch (ClassCastException e) {
					// This is not an array.
					safeJSONTraverseErrorReport(sequence, cursor, original,
						"Cannot access array element: not an array.");
				}
				if (ja == null) {
					// This array is null
					safeJSONTraverseErrorReport(sequence, cursor, original,
						"Cannot access array element: array is null.");
				}
				else {
					try {
						any_json = ja.get(index);
					}
					catch (IndexOutOfBoundsException e) {
						// This array does not have enough elements.
						safeJSONTraverseErrorReport(sequence, cursor, original,
							"Cannot get element " + index + " from array.");
					}
				}
				cursor += array_index_m.end();
			}
			else if (object_m.find() && object_m.start() == 0) {
				// Get an object attribute
				String attribute_name = object_m.group(1);
				JSONObject jo = null;
				try {
					jo = (JSONObject) any_json;
				}
				catch (ClassCastException e) {
					// This is not an object.
					safeJSONTraverseErrorReport(sequence, cursor, original,
						"Cannot get an object attribute: not an object.");
				}
				if (jo == null) {
					// This object is null
					safeJSONTraverseErrorReport(sequence, cursor, original,
						"Cannot access object attribute: "
						+ "object is null.");
				}
				else {
					any_json = jo.get(attribute_name);
					if (any_json == null) {
						// The object doesn't have this attribute.
						safeJSONTraverseErrorReport(sequence, cursor, original,
							"Cannot get attribute " + attribute_name +
							" from object");
					}
				}
				cursor += object_m.end();
			}
			else {
				throw new RuntimeException("BUG: Malformed traversal " +
					sequence + " passed regex.");
			}
		}
		if (any_json == null) {
			safeJSONTraverseErrorReport(
				sequence,
				sequence.length() - 1,
				original,
				"Traversal returned null.");
		}
		if (any_json.getClass().equals(target)) {
			return any_json;
		}
		else {
			safeJSONTraverseErrorReport(
				sequence,
				sequence.length() - 1,
				original,
				"Traversal expected a " + target.getSimpleName() +
				" but received a " + any_json.getClass().getSimpleName());
			// Impossible return to make javac happy:
			return null;
		}
	}

	/**
	 * Execute an Apache Fluent Request.
	 * Decorates HTTP error tracebacks with urls and server {"error": "..."}
	 * responses.
	 * Throws an IOException with URL if the server returns an empty response.
	 * Returns server response if the status code is >= 400
	 *     but can still throw other exceptions if JSON parsing fails when
	 *     formatting server JSON response
	 * @param request
	 * @return the requested string from the server
	 * @throws ClientProtocolException
	 * @throws IOException
	 * @throws RateLimitException
	 */
	public String executeHTTPRequest(Request request)
	throws ClientProtocolException, IOException, RateLimitException {
		//    	System.out.println("execute HTTPRequest in request now: " + request);
		// It's possible we need to reimplement this as a ResponseHandler
		//System.out.println("Sending request: " + request);
		// Execute the HTTP request
		HttpResponse response;
		if (debug)
			System.out.println("Sending request: " + request);
		try {
			response = http_connection.execute(request).returnResponse();
		}
		catch (HttpResponseException e) {
			// Something happened during the request that we can't handle
			System.out.println("Connection error encountered in processing '"
				+ request + "\n");
			throw e;
		}

		//  System.out.println(request);
		//	System.out.println(response);
		/* This is somewhat complicated for getting a string, but:
		 *   ...execute(request).returnContent().asString()
		 *   	won't give error codes
		 *   (String) ...execute(request).returnResponse().getEntity()
		 *   	won't cast
		 */
		//	this will output the server error as well as
		// 	parsed from the error message
		String err = asJSONObject(EntityUtils.toString(
					response.getEntity())).keySet().toString();
		String text = EntityUtils.toString(response.getEntity());
		if (response.getStatusLine().getStatusCode() == 503) {
			throw new RateLimitException("Server responds Service Temporarily"
				+ " Unavailable. You have probably reached your quota."
				+ " Try again after waiting at least 15 minutes.");
		}
		else if (response.getStatusLine().getStatusCode() >= 400) {
			// The request succeeded but the server threw an error
			System.err.println("Server returned error response: HTTP " +
				response.getStatusLine().getStatusCode() + " while"
				+ " processing the request " + request);

			/* By convention, the server responds {"error": "message"} */

			// Parsing it as an object will throw if the server gave an error.
			// asJSONObject(text);

			// But otherwise, throw something less helpful.
			throw new IOException("Server errored, but gave an invalid"
				+ " report: " + text + ". Consider filing a bug report"
				+ " about this at http://github.com/SeanTater/bridges.");
		}

		// Handle empty responses
		if (text == null || text.isEmpty())
			throw new IOException("Server returned empty response for '"
				+ request + "'");
		return text;
	}

	/** Execute a simple GET request relative to the server root.
	    Omit the leading http://hostname, but include the leading /:
	    [good]: /api/followgraph/user/sean
	    [bad]: api/followgraph/user/sean
	    [bad]: http://myserver:9183/api/followgraph/user/sean   NullPointerException*/
	public String get(String url) throws RateLimitException, IOException {

		System.out.println("get Connector url before formatting: " + url);
		String furl = prepare(url);
		System.out.println("From Connector.get()..\n" + furl);
		Request req = Request.Get(furl);
		return executeHTTPRequest(req);
	}


	/**
	 * Execute a request of earthquakes to https://earthquakes-uncc.herokuapp.com/eq/
	 * @param url
	 * @return JSON string
	 * @throws RateLimitException
	 * @throws IOException
	 */
	public String getUSGS(String url) throws RateLimitException, IOException {
		//    	System.out.println("\nGetting earthquakes (the backend connection is working)...\n");
		return executeHTTPRequest(Request.Get(prepareUSGS(url)));
	}

	/** Execute a simple POST request with relative paths, taking a Scala Map()
	    of request parameters. */
	public void post(String url, Map<String, String> arguments)
	throws IOException, RateLimitException {
		//System.out.println("From Connector.post1()..\n");
		Request req = Request.Post(prepare(url));
		Form form = Form.form();
		for (Entry<String, String> e : DataFormatter.sorted_entries(arguments)) {
			form.add(e.getKey(), e.getValue());
		}
		executeHTTPRequest(req.bodyForm(form.build()));
	}

	public void post(String url, String data) throws IOException,
		RateLimitException {
		executeHTTPRequest(Request.Post(prepare(url))
			.bodyString(data, ContentType.TEXT_PLAIN));
	}


	/**
	 * Escape the URL and prepend the base URL.
	 * @returns the new url as a String
	 */
	public String prepare(String url) {
		String out = server_url;
		//    	System.out.println(out);
		out += url
			.replace(" ", "%20")
			.replace("$assignment", Bridges.getAssignment());
		out += "?apikey=" + Bridges.getKey();
		//    	System.out.println(out);
		return out;
	}

	public String prepareUSGS(String url) {
		String out = usgs_url;
		out += url;
		//    	System.out.println(out);
		return out;
	}

}
