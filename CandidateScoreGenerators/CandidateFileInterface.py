"""
This code runs on python 2.4 or later.

By Rob Lyon <robert.lyon@cs.man.ac.uk>

+-----------------------------------------------------------------------------------------+
+                       PLEASE RECORD ANY MODIFICATIONS YOU MAKE BELOW                    +
+-----------------------------------------------------------------------------------------+
+ Revision |   Author    | Description                                       |    DATE    +
+-----------------------------------------------------------------------------------------+

 Revision:0    Rob Lyon    Initial version of the code.                        07/02/2014



+-----------------------------------------------------------------------------------------+

NOTE: You can go directly to a revision by searching the text below i.e. search for "Revision:2b"

"""

# Python 2.4 imports.
from Utilities import Utilities

# ****************************************************************************************************
#
# CLASS DEFINITION
#
# ****************************************************************************************************
    
class CandidateFileInterface(Utilities):
    """
    An interface that defines the functions which a candidate file must implement.
    All candidate files whatever their type must implement these methods. If a new type
    of candidate file appears in the future, then simply create a new candidate class that
    inherits this interface. Then the new candidate file will be usable by this application.
    """
        
    # ****************************************************************************************************
    #
    # Functions.
    #
    # ****************************************************************************************************
    
    def __init__(self,debugFlag):
        """
        Default constructor.
        
        Parameters:
        
        debugFlag    -    the debugging flag. If set to True, then detailed
                          debugging messages will be printed to the terminal
                          during execution.
        """
        Utilities.__init__(self,debugFlag)
        self.numberOfScores = 22 # This is the default - can be set to other values.
        self.epsilon = 0.000005 # Used during score comparison.
    
    # ****************************************************************************************************
    
    def setNumberOfScores(self,n):
        """
        Sets the number of scores a candidate file object should
        be expected to generate.
        
        Parameter:
        n    -    the total number of scores, integer.
        
        Return:
        N/A
        """
        
        self.numberOfScores = int(n)
    
    # ****************************************************************************************************
    
    def filterScore(self,s,value):
        """
        Filters a return score value, so that if it is outside an expected range,
        then the score is corrected, and the corrected version returned.
        
        Parameter:
        s        -    index of the score, i.e. 1,2,3,...,n.
        value    -    the value of the score.
        
        Return:
        The score value if it is valid, else a formatted version of the score.
        """

        if(s==13):# SNR
            if(self.isEqual(value, 0.0, self.epsilon)==-1):
                return 0.0
            else:
                return value
            
        elif(s==14): # DM
            if(self.isEqual(value, 0.0, self.epsilon)==-1):
                return 0.0
            else:
                return value
            
        elif(s==18): # mod(DMfit - DMbest).
            return float(abs(value))
        else:
            return value
    
    # ****************************************************************************************************
    
    def isEqual(self,a,b,epsln):
        """
        Used to compare two floats for equality. This code has to cope with some
        extreme possibilities, i.e. the comparison of two floats which are arbitrarily
        small or large.
        
        Parameters:
        a        -    the first floating point number.
        b        -    the second floating point number.
        epsln    -    the allowable error.
        
        Returns:
        
        A value of -1 if a < b, a value greater than 1 if a > b, else
        zero is returned.
        
        """
        
        # There are two possibilities - both numbers may have exponents,
        # neither may have exponents, or a combination may occur. We need
        # a valid way to compare numbers with these possibilities which fits
        # ALL scenarios. The decision here (right or wrong!) is to avoid
        # wasting time on the perfect solution, and just allow the user to
        # specify an epsilon value they are happy with. In this case we 
        # are assuming a change to the score smaller than epsilon is 
        # effectively meaningless. 
        
        if( abs(a - b) > epsln):
            if( a < b):
                return -1
            else:
                return 1 
        else:
            return 0
        
    # ****************************************************************************************************
    
    def compute(self):
        raise NotImplementedError("Please Implement this method")
    
    # ****************************************************************************************************
           
    def load(self):
        raise NotImplementedError("Please Implement this method")
    
    # ****************************************************************************************************
    
    def getProfile(self):
        raise NotImplementedError("Please Implement this method")
    
    # ****************************************************************************************************
    
    def isValid(self):
        raise NotImplementedError("Please Implement this method")
    
    # ****************************************************************************************************
    
    def computeSinusoidFittingScores(self):
        raise NotImplementedError("Please Implement this method")
    
    # ****************************************************************************************************
    
    def computeGaussianFittingScores(self):
        raise NotImplementedError("Please Implement this method")
    
    # ****************************************************************************************************
    
    def computeCandidateParameterScores(self):
        raise NotImplementedError("Please Implement this method")
    
    # ****************************************************************************************************
    
    def computeDMCurveFittingScores(self):
        raise NotImplementedError("Please Implement this method")
    
    # ****************************************************************************************************
    
    def computeSubBandScores(self):
        raise NotImplementedError("Please Implement this method")
    
    # ****************************************************************************************************