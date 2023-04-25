def isValidString(s):
  if len(s.strip()) == 0:
      return False

  

  while((len(s) != 0)):
      #checks if the string starts with Q
      if s[0] != 'Q':
          return False
      
      s = s[1:len(s)]
      i = 0
      
      #section checks for the batch length
      batchLen = ''
      for c in s:
          if c.isdigit():
            batchLen = batchLen + c
            i = i + 1
          else:
              break
    
    # if batchlen starts with a leading zero then fail
      if len(batchLen) > 1 and batchLen[0] == '0':
          return False
      
      totalBatchSize = int(batchLen)

    #if batchsize is zero then return false
      if totalBatchSize == 0:
         return False

    #gets the substring after reading batch length
      s = s[i:len(s)]

      
    #if string  doesn't   start with p or d then it is invalid 
      if s[0] != 'p' and s[0] != 'd':
        return False
      
    #read substring after getting the p or d
      s = s[1:len(s)]
      
      #section is to get length of the test and sum it
      i = 0
      testLen = ''
      totalNumberOfTests = 0
    
      for c in s:
          if c.isdigit():
              testLen = testLen + c
              i = i+1
          else:
              break
          
    #if test length is greater than 1 digit but starts with a zero, the string is invalid
      if len(testLen) > 1 and testLen[0] == '0':
        return False
      
      totalNumberOfTests += int(testLen)

    #get next substring after reading that test len
      s = s[i:len(s)]
      

#check for p or d
      if s[0] != 'p' and s[0] != 'd':
        return False
      
      #get next substring to check for the length
      s = s[1:len(s)]
      i = 0
      testLen = ''
    
    #section to check for the length
      for c in s:
          if c.isdigit():
              testLen = testLen + c
              i = i+1
          else:
              break
          
    #if test length is greater than 1 digit but starts with a zero, the string is invalid
      if len(testLen) > 1 and testLen[0] == '0':
        return False
      
      totalNumberOfTests += int(testLen)

#check if total batch size is not the same as test length and return invalid
      if(totalBatchSize != totalNumberOfTests):
          return False
      
      #get the next substring
      s = s[i:len(s)]

  return True