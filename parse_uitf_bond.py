import re

def twod_list(txtfile):
    """
    returns a 2d list of the uitf copied data.
    it must not contain empty lines
    :param txtfile: copied data from http://www.uitf.com.ph
    :returns: 2d list of the uitf copied data
    """
    mylist=[]
    f=open(txtfile,'r')
    ct=0
    lev1=[]
    for x in f:
        if ct > 3:
            mylist.append(lev1)
            lev1=[]
            lev1.append(re.sub('\n','',x))
            ct=1
        else:
            lev1.append(re.sub('\n','',x))
            ct+=1

    return mylist

if __name__=="__main__":
    mylist=twod_list('uitf00.txt')
    print('halt')
