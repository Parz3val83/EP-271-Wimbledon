#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This Python module contains functions that fit different
mathematical models to a set of data.
"""

def poly_fit(dataset,degree,plotit=False):
    """
    This Python 3 function performs polynomial fitting of the data
    set that is passed through the dataset argument.  Optionally,
    it displays a plot of the data and the fitted curve.
    This function also prints the R^2 measure of the fit quality.

    Parameters
    ----------
    dataset : 2D NumPy array of floating-point numbers
        Dataset provides the independent-coordinate and dependent
        variable for each data point with one data point per
        row of the 2D array.
    degree : integer
        Degree determines the degree of the polynomial that is
        used to fit the data.
    plotit : Boolean (optional)
        Plotit indicates whether to create a plot.

    Returns
    -------
    coeffs : 1D NumPy array
        The coeffs array returns the coefficients of the polynomial
        fit, starting with the coefficient of the x^0 monomial and
        ending with the x^degree monomial.
    """
    
    import numpy as np
    
    # Get the number of points in the data set.
    
    ndata=dataset.shape[0]
    
    # Generate the matrix of terms that is sent to the least-squares
    # NumPy function.  Note that the first column is 1, the second
    # is the dataset independent coordinates to the first power (x_i^1),
    # the third is x_i^2, and so on.

    tmat=np.ones((ndata,degree+1))
    for j in range (1,degree+1):
        tmat[:,j]=dataset[:,0]*tmat[:,j-1]

    # Use NumPy's lstsq function from its linalg module to solve
    # the least-squares problem.

    rhs=np.copy(dataset[:,1])  #  extracts the dependent-variable data
#   coeffs=np.linalg.lstsq(tmat,rhs,rcond=-1.)[0]
    coeffs=np.linalg.lstsq(tmat,rhs,rcond=None)[0]  #  For new linalg module
    
    # Compute and print the R^2 value.  Generate the model's predictions
    # at the data's independent coordinates, then perform the R^2
    # computation.

    ymodel=np.zeros(ndata)
    for pwr in range(degree+1):
        ymodel+=coeffs[pwr]*dataset[:,0]**pwr
    yave=np.mean(dataset[:,1])
    r2=1-np.sum((ymodel-dataset[:,1])**2)/np.sum((yave-dataset[:,1])**2)
    
    print('\nThe R2 value of the degree %d polynomial fit is %14.8f.\n'
          % (degree,r2))

    # Peform the optional plotting if requested.  First, generate a curve
    # to show the fit.

    if plotit:
        nplt=51  #  First generate a curve to show the fit.
        xmin=np.min(dataset[:,0])
        xmax=np.max(dataset[:,0])
        xplt=np.linspace(xmin-(xmax-xmin)*0.02,xmax+(xmax-xmin)*0.02,nplt)
        yplt=np.zeros(nplt)
        for pwr in range(degree+1):
            yplt+=coeffs[pwr]*xplt**pwr
        fit_plot(dataset,xplt,yplt)
        
    return coeffs


def exp_fit(dataset,plotit=False):
    """
    This Python 3 function performs exponential fitting of the data
    set that is passed through the dataset argument.  Optionally,
    it displays a plot of the data and the fitted curve.
    This function also prints the R^2 measure of the fit quality.

    Parameters
    ----------
    dataset : 2D NumPy array of floating-point numbers
        Dataset provides the independent-coordinate and dependent
        variable for each data point with one data point per
        row of the 2D array.
    plotit : Boolean (optional)
        Plotit indicates whether to create a plot.

    Returns
    -------
    coeffs : 1D NumPy array
        The coeffs array returns the coefficients of the exponential
        fit.  For the exponential model, K*exp(lambda*x), the
        coeffs array is [K  lambda].
    """
    
    import numpy as np
    
    # Get the number of points in the data set.
    
    ndata=dataset.shape[0]
    
    # Generate the matrix of terms that is sent to the least-squares
    # NumPy function.  The least-squares equation is for ln(K) and
    # lambda.  The rhs of the least-squares problem is the logarithm
    # of the data's dependent-variable values.  The matrix of terms
    # has 1 in the entire first column and the independent coordinate
    # values in the second column.

    tmat=np.ones((ndata,2))
    tmat[:,1]=dataset[:,0]

    # Use NumPy's lstsq function from its linalg module to solve
    # the least-squares problem.

    rhs=np.log(dataset[:,1])
#   coeffs=np.linalg.lstsq(tmat,rhs,rcond=-1.)[0]
    coeffs=np.linalg.lstsq(tmat,rhs,rcond=None)[0]  #  For new linalg module

    coeffs[0]=np.exp(coeffs[0])  #  Undo the logarithm of K.
    
    # Compute and print the R^2 value.  Generate the model's predictions
    # at the data's independent coordinates, then perform the R^2
    # computation.

    ymodel=coeffs[0]*np.exp(coeffs[1]*dataset[:,0])
    yave=np.mean(dataset[:,1])
    r2=1-np.sum((ymodel-dataset[:,1])**2)/np.sum((yave-dataset[:,1])**2)
    
    print('\nThe R2 value of the exponential fit is %14.8f.\n'
          % (r2))

    # Peform the optional plotting if requested.  First, generate a curve
    # to show the fit.

    if plotit:
        nplt=51  #  First generate a curve to show the fit.
        xmin=np.min(dataset[:,0])
        xmax=np.max(dataset[:,0])
        xplt=np.linspace(xmin-(xmax-xmin)*0.02,xmax+(xmax-xmin)*0.02,nplt)
        yplt=np.zeros(nplt)
        yplt=coeffs[0]*np.exp(coeffs[1]*xplt)
        fit_plot(dataset,xplt,yplt)
        
    return coeffs

def gauss_fit(dataset,plotit=False):
    """
    This Python 3 function performs a normal distribution fitting of the data
    set that is passed through the dataset argument.  Optionally,
    it displays a plot of the data and the fitted curve.

    Parameters
    ----------
    dataset : 2D NumPy array of floating-point numbers
        Dataset provides the independent-coordinate and dependent
        variable for each data point with one data point per
        row of the 2D array.
    plotit : Boolean (optional)
        Plotit indicates whether to create a plot.

    Returns
    -------
    coeffs : 1D NumPy array
        The coeffs array returns the coefficients of the normal fit
        fit.  For the normal-fit model, A * exp(-(x-Mu)**2/sigma**2), the
        coeffs array is [A Mu sigma].
    """

    import numpy as np
    #Defining the gaussian function
    

    #Generating the matrix to be optimized in X * P = Y
    X = np.ones((dataset.shape[0],3))
    X[:, 1] = dataset[:,0]
    X[:, 2] = dataset[:,0]**2

    #Solving for P and extracting the coefficients
    params = np.linalg.lstsq(X, dataset[:,1], rcond=None)[0]

    #Solving for A, mu, and sigma from params
    sigma = np.sqrt(-1/(params[2]))
    mu = (params[1] * sigma)/2
    A = np.exp(params[0] + (mu**2/sigma**2))

    if plotit:
        nplt=51  #  First generate a curve to show the fit.
        xmin=np.min(dataset[:,0])
        xmax=np.max(dataset[:,0])
        xplt=np.linspace(xmin-(xmax-xmin)*0.02,xmax+(xmax-xmin)*0.02,nplt)
        yplt=np.zeros(nplt)
        yplt=np.exp(-(x-mu)**2/sigma**2)
        fit_plot(dataset,xplt,yplt)

    returns = [A, mu, sigma]
    #if plotit: plt.show()
    return(returns)

def power_fit(dataset,plotit=False):
    """
    This Python 3 function performs power-law fitting of the data
    set that is passed through the dataset argument.  Optionally,
    it displays a plot of the data and the fitted curve.
    This function also prints the R^2 measure of the fit quality.

    Parameters
    ----------
    dataset : 2D NumPy array of floating-point numbers
        Dataset provides the independent-coordinate and dependent
        variable for each data point with one data point per
        row of the 2D array.
    plotit : Boolean (optional)
        Plotit indicates whether to create a plot.

    Returns
    -------
    coeffs : 1D NumPy array
        The coeffs array returns the coefficients of the power-law
        fit.  For the power-law model, K*x**alpha, the
        coeffs array is [K  alpha].
    """
    
    import numpy as np
    
    # Get the number of points in the data set.
    
    ndata=dataset.shape[0]
    
    # Generate the matrix of terms that is sent to the least-squares
    # NumPy function.  The least-squares equation is for ln(K) and
    # alpha.  The rhs of the least-squares problem is the logarithm
    # of the data's dependent-variable values.  The matrix of terms
    # has 1 in the entire first column and the logarithm of the
    # independent coordinate values in the second column.

    tmat=np.ones((ndata,2))
    tmat[:,1]=np.log(dataset[:,0])

    # Use NumPy's lstsq function from its linalg module to solve
    # the least-squares problem.

    rhs=np.log(dataset[:,1])
#   coeffs=np.linalg.lstsq(tmat,rhs,rcond=-1.)[0]
    coeffs=np.linalg.lstsq(tmat,rhs,rcond=None)[0]  #  For new linalg module

    coeffs[0]=np.exp(coeffs[0])  #  Undo the logarithm of K.
    
    # Compute and print the R^2 value.  Generate the model's predictions
    # at the data's independent coordinates, then perform the R^2
    # computation.

    ymodel=coeffs[0]*dataset[:,0]**coeffs[1]
    yave=np.mean(dataset[:,1])
    r2=1-np.sum((ymodel-dataset[:,1])**2)/np.sum((yave-dataset[:,1])**2)
    
    print('\nThe R2 value of the power-law fit is %14.8f.\n'
          % (r2))

    # Peform the optional plotting if requested.  First, generate a curve
    # to show the fit.

    if plotit:
        nplt=51  #  First generate a curve to show the fit.
        xmin=np.min(dataset[:,0])
        xmax=np.max(dataset[:,0])
        xplt=np.linspace(xmin-(xmax-xmin)*0.02,xmax+(xmax-xmin)*0.02,nplt)
        yplt=np.zeros(nplt)
        yplt=coeffs[0]*xplt**coeffs[1]
        fit_plot(dataset,xplt,yplt)
        
    return coeffs


def fit_plot(dataset,xfit,yfit):
    """
    This Python 3 function make a plot of the data and
    a curve that represents the fitted data.

    Parameters
    ----------
    dataset : 2D NumPy array of floating-point numbers
        Dataset provides the independent-coordinate and dependent
        variable for each data point with one data point per
        row of the 2D array.
    xfit : 1D NumPy array of floating-point numbers
        Xfit holds the independent-coordinate values for the
        fitted curve.
    yfit : 1D NumPy array of floating-point numbers
        Yfit holds the dependent-variable values for the
        fitted curve.

    Returns
    -------
    Nothing  (It generates the plot, however.)
    """
    
    import matplotlib.pyplot as plt

    plt.figure(figsize=[5.,4.])
    plt.subplots_adjust(left=0.17,bottom=0.14,top=0.94,right=0.94)
    plt.plot(dataset[:,0],dataset[:,1],'b*',markersize=8)
    plt.plot(xfit,yfit,'r',linewidth=2)
    plt.legend(['data points','fit'],fontsize=13)
    plt.xlabel('X',fontsize=14)
    plt.ylabel('Y',fontsize=14)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.show()
    
    return
