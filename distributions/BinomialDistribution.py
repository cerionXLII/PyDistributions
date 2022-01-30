import math
import matplotlib.pyplot as plt
import numpy as np
from .GeneralDistribution import Distribution

class Binomial(Distribution):
    def __init__(self, prob = 0.5, n=100):
        print('Made Binomial')
        self.p = prob
        self.n = n

        mu = self.calculate_mean()
        std = self.calculate_stdev()

        Distribution.__init__(self, mu, std)

    def calculate_mean(self):
        self.mean = self.p * self.n
        return self.mean


    def calculate_stdev(self):
        self.stdev = np.sqrt(self.n * self.p * ( 1.0 - self.p))
        return self.stdev
    
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        
        self.n = len(self.data)
        self.p = np.average(self.data) #Assumes we have a distribution of ones and zeros
        self.calculate_mean()
        self.calculate_stdev()

        return self.p, self.n

        
        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        x = ['0', '1']
        y = [(1.0 - self.p) * self.n, self.p * self.n]

        plt.bar(x=x, height=y)
        plt.title('Bar chart of data')
        plt.xlabel('Outcome')
        plt.ylabel('Frequency')

            
      
        
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        b = (self.p ** k) * (1 - self.p) ** (self.n - k)
        
        return a * b

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """

        x = np.arange(0, self.n, 1)
        y = [self.pdf(k) for k in x]
    
        plt.bar(x, y)
        plt.title('Probability distribution')
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.show()
        
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        n = self.n + other.n
        return Binomial(self.p, n)
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        return f'mean: {self.mean}, std: {self.stdev}'
       
