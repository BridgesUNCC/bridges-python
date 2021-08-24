class CancerIncidence:
    """
    @brief A class representing the attributes for cancer incidence.

    From the United States Cancer Statistics as part of the U.S. Center for
    Disease Control, the following data set focuses on the crude rate for
    all types of cancer reported for different demograpic groups.
    Significant groupings include age, gender, race and geographical area.

    For an example, check out https://bridgesuncc.github.io/tutorials/Data_CancerIncidence.html
    
    This object is generally not created by the user, to see how its created check 
    out bridges::data_src_dependent::data_source::get_cancer_incident_data()
      
    http://www.cdc.gov/cancer/npcr/uscs/download_data.htm
    Data: Courtesy of Corgis Datasets, 2017
   
    @author Kalpathi Subramanian
    @date 2017, 12/29/20
    """
    def __init__(self):
        self.loc = []
        self.year = 0
        self.count = 0
        self.population = 0
        self.gender = ""
        self.race = ""
        self.event_type = ""
        self.affected_area = ""
        self.ageAdjustedRate = 0.0
        self.crudeRate = 0.0
        self.loc.append(0.0)
        self.loc.append(0.0)
        self.ageAdjustedRateci= []
        self.crudeRateci = []
        self.ageAdjustedRateci.append(0.0)
        self.ageAdjustedRateci.append(0.0)
        self.crudeRateci.append(0.0)
        self.crudeRateci.append(0.0)

    def get_age_adjusted_rate(self):
        return self.ageAdjustedRate

    def set_age_adjusted_rate(self, arr):
        self.ageAdjustedRate = arr

    def get_age_adjusted_ci_lower(self):
        return self.ageAdjustedRateci[0]

    def set_age_adjusted_ci_lower(self, ci_l):
        self.ageAdjustedRateci[0] = ci_l

    def get_age_adjusted_ci_upper(self):
        return self.ageAdjustedRateci[1]

    def set_age_adjusted_ci_upper(self, ci_u):
        self.ageAdjustedRateci[1] = ci_u

    def get_crude_rate(self):
        return self.crudeRate

    def set_crude_rate(self, cr):
        self.crudeRate = cr

    def get_crude_rate_ci_lower(self):
        return self.crudeRateci[0]

    def set_crude_rate_ci_lower(self, cr_l):
        self.crudeRateci[0] = cr_l

    def get_crude_rate_ci_upper(self):
        return self.crudeRateci[1]

    def set_crude_rate_ci_upper(self, cr_l):
        self.crudeRateci[1] = cr_l

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_race(self):
        return self.race

    def set_race(self, race):
        self.race = race

    def get_event_type(self):
        return self.event_type

    def set_event_type(self, et):
        self.event_type = et

    def get_population(self):
        return self.population

    def set_population(self, pop):
        self.population = pop

    def get_affected_area(self):
        return self.affected_area

    def set_affected_area(self, area):
        self.affected_area = area

    def get_count(self):
        return self.count

    def set_count(self,count):
        self.count = count

    def get_location_x(self):
        return self.loc[0]

    def set_location_x(self, x):
        self.loc[0] = x

    def get_location_y(self):
        return self.loc[1]

    def set_location_y(self, y):
        self.loc[1] = y
