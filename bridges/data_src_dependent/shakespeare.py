
class Shakespeare:
    """
    @brief  A Shakespeare Data source object containing sonnets, poems and plays
   
    This is a convenience class provided for  users who wish to use this
    data source as part of their application. It provides an API that makes
    it easy to access the attributes of this data set.
    
    Refer to tutorial examples to using this data source in data structure
    assignments.

    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_shakespeare_data()

    For an example, check out https://bridgesuncc.github.io/tutorials/Data_Shakespeare.html

    @author Matthew Mcauaigue, Kalpathi Subramanian

    @date   2018, 12/28/20
    """
    ##
    #    @param title title of sonnet, play or poem
    #    @param type sonnet, play or poem
    #    @param text full text of work
    #
    def __init__(self, title: str = "", type: str = "", text: str = ""):
        self._title = title
        self._type = type
        self._text = text

    ## 
    # @brief Get title
    #
    @property
    def title(self):
        return self._title

    ##
    # @brief set title
    # @param t title of work
    #
    @title.setter
    def title(self, t):
        self._title = t

    ## 
    # @brief Get type (sonnet, play or poem)
    #
    @property
    def type(self):
        return self._type

    ##
    # @brief set type of work (sonnet, play or poem)
    # @param t type of work
    #
    @type.setter
    def type(self, t):
        self._type = t

    ## 
    # @brief Get text of sonnet, play or poem
    #
    @property
    def text(self):
        return self._text

    ##
    # @brief set full text of work
    # @param t full text
    #
    @text.setter
    def text(self, t):
        self._text = t
