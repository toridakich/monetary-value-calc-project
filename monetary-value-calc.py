import re

#Get data
import requests
r = requests.get("https://questionnaire-148920.appspot.com/swe/data.html")



from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('tr')

salaries = []
for result in results:
    x = result.find('td', attrs={'class':'player-salary'}).text
    x = re.sub('[$]', '', x)


    if(x != 'no salary data' and x != ''):
        salaries.append(int(x.replace(",", "")))


    
#Function definitions
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )

def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)

def findAverage(arr):
    salarySum = 0
    for x in range(125):
        salarySum = salarySum + arr[x*(-1)]
    return salarySum // 125


#Main

quickSort(salaries, 0, len(salaries)-1)
z = findAverage(salaries)
print("moneary value: $" + "{:,}".format(z))

#Stack Overflow source for error handling: https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
