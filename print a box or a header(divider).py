#to know how this works read the bottom part

def linecr(mo="_",rep=1,spa=2,cdis="",center=0,lineremov=0,specialfeature=0,middlepart=12,lineaftersentence=0,adjuster=0,ychar="┆"):
    if cdis!="":
        k=(rep*2)+1
    else:
        k=rep 
    middlepart=str(middlepart)   
    ja=cdis
    if cdis!="":
        for hoho in range(k):
            if hoho<(k//2) or (hoho>(k//2) and lineremov==0):
                if specialfeature==0:
                     print(mo*98)
                else:
              
                    
                    if hoho==(k-1):
                        print(f"{'╹'+(mo*96)+'╹'}")
                    else:
                       print(f"{'╷'+(mo*96)+'╷'}")
                
                    
            elif(hoho==(k//2)):
              if specialfeature==0:
                if center==0:
                     print(ja)
                else:
                    
                    print(" "*41+ja)
              else:
                  if middlepart.isalpha() is True and middlepart.lower()=='max':
                            middlepart=55
                  else:
                    if middlepart.isalpha() is False and int(middlepart)>55:
                        middlepart=12
                          
                  cdis=cdis.split("\n")
                  middlepart=int(middlepart)
                  for ik in cdis:
                      ik=ik.split('\\{1}')
                      if len(ik)==2:
                          if adjuster>0:
                              fornow=adjuster
                          else:
                              fornow=41  
                          if middlepart>53:
                              middlepart=53
                          if len(ik[0])>middlepart:
                              ik=list(ik[0])
                              for start in range(0, len(ik), middlepart):
                                     print(f'{ychar+" " +(" "*fornow)+"".join(ik[start:start+middlepart]) +(((96-(middlepart+(fornow+2)))*" ")+(middlepart-len("".join(ik[start:start+middlepart])))*" ")+" "+ychar}')
                              

                          else:
    
                             print(f'{ychar+" "+(" "*fornow)+ik[0]+(((96-(len(ik[0])+(fornow+2)))*" ")+" "+ychar)}')
                              

                         
                      elif len(ik)==1:
                          if len(ik[0])>96:
                              ik=list(ik[0])
                              for start in range(0, len(ik), 94):
                                     print(f'{ychar+" " + "".join(ik[start:start+94]) +(94-len("".join(ik[start:start+94])))*" "+" "+ychar}')
                          else:
                              print(f'{ychar+" "+ik[0]+((94-len(ik[0]))*" ")+" "+ychar}')
                      if lineaftersentence>0:
                         for lisass in range(lineaftersentence):
                              print(f"{ychar+(96*' ')+ychar}")
                          
                              
                    
    else:           
        for hoho in range(k):
            print(mo*98)
    
    if spa==0:
        pass
    elif spa==1:
        print()
    
    elif spa==2:
        print()
        print()

    elif(spa>=3):
          print()
          print()
          print()
          



#The function ends here.Read below to know how to use the function



"""
EXAMPLES :
 SECTION-
  ex 1: linecr("-")
  
  ex 2: linecr("-",2,2,'example',1)
  
  ex 3: linecr("=",1,2,'example \nHello!! how are you?? \n :D',0,0,1)
 
"""

"""
SECTION-0:
  #This section is only for printing lines
  Use this call- linecr("characteroftheline",numberoftimestoberepeated,spacesaftertheline)
  
  #Examples:
     call:
        1: linecr("-")
        
        O/P(1)-
            --------------------------------------------------------------------------------------------------
        
        2: linecr("-",2)  
        
        O/P(2)-
           --------------------------------------------------------------------------------------------------
           --------------------------------------------------------------------------------------------------
       

SECTION-1:
  *note : make different lines in a message by using '\n'..Ex- "Hello!!\nHow are you"
  *note : if you are using this particular feature then make sure each line in the message should have at most 98 characters!!(as I haven't designed a code that will check that)
          and if you are using the center then make sure the center line/lines have at most 57 characters.
           
   #This deals with the following outputs-

          O/P(1)-
          
             --------------------------------------------------------------------------------------------------
                                                      example
             --------------------------------------------------------------------------------------------------


          O/P(2)-
             --------------------------------------------------------------------------------------------------
             example
             --------------------------------------------------------------------------------------------------
          
          
          O/P(3)-
             --------------------------------------------------------------------------------------------------
                                                      example       
          
          O/P(4)-
            --------------------------------------------------------------------------------------------------
            example

              

       *calls used for the outputs above :
           (1)- linecr("-",2,2,'example',1)
           (2)- linecr("-",2,2,'example',0) / linecr("-",2,2,'example')
           (3)- linecr("-",2,2,'example',1,1)
           (4)- linecr("-",2,2,'example',0,1)

   #mo is the character used to make the line 
   
   #rep is the amount of times you want to repeat the horizontal line
   
   #spa is for space after the message has been displayed.Basically the default value is 2 so it will print 2 empty lines.
    Value 1 will print 1 empty line and Value >= 3 will print 3 empty lines.value 0 will print no empty lines 
    
   #cdis is a custom display option that will display messages
   
   #center is to see if you want the custom display to be displayed in the center or near the start.It has been disabled by default.
    
   #lineremov is if you dont want a line printed after the message.It has been disabled by default i.e the line will be there.




SECTION-2
     *note- Everything is same as SECTION-1 except center and lineremov don't work so it is better to leave them as their default values.
            Plus this will format the sentences on its own so no need to worry about character space and all.
     
     #This deals with the following outputs:
              
               O/P(1)-
                  ╷================================================================================================╷
                  ┆ example                                                                                        ┆
                  ╹================================================================================================╹ 
               
               O/P(2)-
                  ╷================================================================================================╷
                  ┆ example                                                                                        ┆
                  ┆ Hello!! how are you??                                                                          ┆
                  ┆  :D                                                                                            ┆
                  ╹================================================================================================╹
                  
                  
               O/P(3)-
                   ╷================================================================================================╷
                   ┆                                          example                                               ┆
                   ┆                                          Hello!! how                                           ┆
                   ┆                                          are you??                                             ┆
                   ┆  :D                                                                                            ┆
                   ╹================================================================================================╹
                  
                  
               O/P(4)-
                   ╷================================================================================================╷
                   ┆                                          example                                               ┆
                   ┆                                          Hello!! how are you??                                 ┆
                   ┆                                                                                                ┆ 
                   ┆  :D                                                                                            ┆
                   ╹================================================================================================╹   
                
                             
               O/P(5)-
                 ╷================================================================================================╷
                 ┆                                          We're no strangers to love You know the rules and so  ┆
                 ┆                                          do I A full commitment's what I'm thinking of.You wou ┆
                 ┆                                          ldn't get this from any other guy...                  ┆
                 ╹================================================================================================╹
                  
                  
               O/P(6)-
                  ╷================================================================================================╷
                  ┆                                          We're no strangers to love                            ┆
                  ┆                                                                                                ┆
                  ┆                                          You know the rules and so do I                        ┆
                  ┆                                                                                                ┆
                  ┆                                          A full commitment's what I'm thinking of.             ┆
                  ┆                                                                                                ┆
                  ┆                                          You wouldn't get this from any other guy...           ┆
                  ┆                                                                                                ┆
                  ┆                                           :D                                                   ┆
                  ┆                                                                                                ┆
                  ╹================================================================================================╹
               
               
               O/P(7)-
                    ╷================================================================================================╷
                    ┆            We're no strangers to love                                                          ┆
                    ┆                                                                                                ┆
                    ┆            You know the rules and so do I                                                      ┆
                    ┆                                                                                                ┆
                    ┆            A full commitment's what I'm thinking of.                                           ┆
                    ┆                                                                                                ┆
                    ┆            You wouldn't get this from any other guy...                                         ┆
                    ┆                                                                                                ┆
                    ┆             :D                                                                                 ┆
                    ┆                                                                                                ┆
                    ╹================================================================================================╹         
               
               
              call:
                 (1)- linecr("=",1,2,'example',0,0,1)
                 (2)- linecr("=",1,2,'example \nHello!! how are you?? \n :D',0,0,1)
                 (3)- linecr("=",1,2,'example \\{1} \nHello!! how are you?? \\{1}\n :D',0,0,1)
                 (4)- linecr("=",1,2,'example \\{1} \nHello!! how are you?? \\{1}\n :D',0,0,1,21)
                 (5)- linecr("=",1,2,"We're no strangers to love You know the rules and so do I A full commitment's what I'm thinking of.You wouldn't get this from any other guy... \\{1}",0,0,1,'max')
                 (6)- linecr("=",1,2,"We're no strangers to love \\{1} \nYou know the rules and so do I \\{1}\nA full commitment's what I'm thinking of.\\{1}\nYou wouldn't get this from any other guy... \\{1} \n :D \\{1}",0,0,1,'max',1)
                 (7)- linecr("=",1,2,"We're no strangers to love \\{1} \nYou know the rules and so do I \\{1}\nA full commitment's what I'm thinking of.\\{1}\nYou wouldn't get this from any other guy... \\{1} \n :D \\{1}",0,0,1,'max',1,11)
     
     
     # you can write a custom message and replace it with the one I wrote
    
     #if you are using the specialfeature then remember the sentences in cdis will be split according to '\n'
    
     #in specialfeature if cdis sentences(lines) have '\\{1}' at the end(don't put this anywhere else) i.e just before the '\n' 
       or at the end then the sentences will be printed in the center of the box.
    
     #middlepart is used for increasing the range of characters that are printed in the middle.Use 'max' or 55 as 55 is the maximum value it can have.
    
     #lineaftersentence is the amount of spaces you want after each line.By default it is 0
    
     #adjuster is used for adjusting the center part's length i.e bringing it closer to the beginning.
    
     #ychar is the character that is used to make the rowlines.
      *note : in specialfeature,mo is used for making columnlines.    
"""

    
