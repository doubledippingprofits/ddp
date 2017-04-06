'''
Created on Apr 5, 2017

@author: Jared
'''

import urllib2

sp500 = ['A','AA','AAPL','ABC','ABT','ACE','ACN','ADBE','ADI','ADM','ADP','ADSK','ADT','AEE','AEP','AES','AET','AFL','AGN','AIG','AIV','AIZ','AKAM','ALL','ALTR','ALXN','AMAT','AMD','AMGN','AMP','AMT','AMZN','AN','ANF','AON','APA','APC','APD','APH','APOL','ARG','ATI','AVB','AVP','AVY','AXP','AZO','BA','BAC','BAX','BBBY','BBT','BBY','BCR','BDX','BEAM','BEN','BF.B','BHI','BIG','BIIB','BK','BLK','BLL','BMC','BMS','BMY','BRCM','BRK.B','BSX','BTU','BWA','BXP','C','CA','CAG','CAH','CAM','CAT','CB','CBG','CBS','CCE','CCI','CCL','CELG','CERN','CF','CFN','CHK','CHRW','CI','CINF','CL','CLF','CLX','CMA','CMCSA','CME','CMG','CMI','CMS','CNP','CNX','COF','COG','COH','COL','COP','COST','COV','CPB','CRM','CSC','CSCO','CSX','CTAS','CTL','CTSH','CTXS','CVC','CVH','CVS','CVX','D','DD','DE','DELL','DF','DFS','DG','DGX','DHI','DHR','DIS','DISCA','DLTR','DNB','DNR','DO','DOV','DOW','DPS','DRI','DTE','DTV','DUK','DVA','DVN','EA','EBAY','ECL','ED','EFX','EIX','EL','EMC','EMN','EMR','EOG','EQR','EQT','ESRX','ESV','ETFC','ETN','ETR','EW','EXC','EXPD','EXPE','F','FAST','FCX','FDO','FDX','FE','FFIV','FHN','FII','FIS','FISV','FITB','FLIR','FLR','FLS','FMC','FOSL','FRX','FSLR','FTI','FTR','GAS','GCI','GD','GE','GILD','GIS','GLW','GME','GNW','GOOG','GPC','GPS','GS','GT','GWW','HAL','HAR','HAS','HBAN','HCBK','HCN','HCP','HD','HES','HIG','HNZ','HOG','HON','HOT','HP','HPQ','HRB','HRL','HRS','HSP','HST','HSY','HUM','IBM','ICE','IFF','IGT','INTC','INTU','IP','IPG','IR','IRM','ISRG','ITW','IVZ','JBL','JCI','JCP','JDSU','JEC','JNJ','JNPR','JOY','JPM','JWN','K','KEY','KIM','KLAC','KMB','KMI','KMX','KO','KR','KRFT','KSS','L','LEG','LEN','LH','LIFE','LLL','LLTC','LLY','LM','LMT','LNC','LO','LOW','LRCX','LSI','LTD','LUK','LUV','LYB','M','MA','MAR','MAS','MAT','MCD','MCHP','MCK','MCO','MDLZ','MDT','MET','MHP','MJN','MKC','MMC','MMM','MNST','MO','MOLX','MON','MOS','MPC','MRK','MRO','MS','MSFT','MSI','MTB','MU','MUR','MWV','MYL','NBL','NBR','NDAQ','NE','NEE','NEM','NFLX','NFX','NI','NKE','NOC','NOV','NRG','NSC','NTAP','NTRS','NU','NUE','NVDA','NWL','NWSA','NYX','OI','OKE','OMC','ORCL','ORLY','OXY','PAYX','PBCT','PBI','PCAR','PCG','PCL','PCLN','PCP','PCS','PDCO','PEG','PEP','PETM','PFE','PFG','PG','PGR','PH','PHM','PKI','PLD','PLL','PM','PNC','PNR','PNW','POM','PPG','PPL','PRGO','PRU','PSA','PSX','PWR','PX','PXD','QCOM','QEP','R','RAI','RDC','RF','RHI','RHT','RL','ROK','ROP','ROST','RRC','RRD','RSG','RTN','S','SAI','SBUX','SCG','SCHW','SE','SEE','SHW','SIAL','SJM','SLB','SLM','SNA','SNDK','SNI','SO','SPG','SPLS','SRCL','SRE','STI','STJ','STT','STX','STZ','SWK','SWN','SWY','SYK','SYMC','SYY','T','TAP','TDC','TE','TEG','TEL','TER','TGT','THC','TIE','TIF','TJX','TMK','TMO','TRIP','TROW','TRV','TSN','TSO','TSS','TWC','TWX','TXN','TXT','TYC','UNH','UNM','UNP','UPS','URBN','USB','UTX','V','VAR','VFC','VIAB','VLO','VMC','VNO','VRSN','VTR','VZ','WAG','WAT','WDC','WEC','WFC','WFM','WHR','WIN','WLP','WM','WMB','WMT','WPI','WPO','WPX','WU','WY','WYN','WYNN','X','XEL','XL','XLNX','XOM','XRAY','XRX','XYL','YHOO','YUM','ZION','ZMH']


def stockFilter(stock):
    '''
        Use this to dynamically pull a stock:
    '''
    try:
        #range=2d can be changed to anything like 14d (14 days), 2m (2 months), or 10y (10 years)
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=2d/csv'
        
        '''
            Filter Settings
        '''
        
        volume = 1000000
        price = 11.0000
        
        try:
            sourceCode = urllib2.urlopen(urlToVisit).read()
            splitSource = sourceCode.split('\n')
            for eachLine in splitSource:
                splitLine = eachLine.split(':')
                if 'previous_close:' in eachLine:
                    
                    if float(splitLine[1]) < price:
                        
                        sourceCode2 = urllib2.urlopen(urlToVisit).read()
                        splitSource2 = sourceCode2.split('\n')
                        for eachLine2 in splitSource2:
                            splitLine2 = eachLine2.split(',')
                            if 'volume:' in eachLine2:
                                if int(splitLine2[1]) > volume:

                                    print stock,'Penny stock with greater than 1,000,000 volume!'
                      
        except Exception, e:
            print str(e), 'failed to organize pulled data.'
    except Exception,e:
        print str(e), 'failed to pull pricing data'
       


for stock in sp500:    
    stockFilter(stock)