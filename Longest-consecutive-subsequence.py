# Longest consecutive subsequence 

# Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

array = [ 2 , 6 , 1 , 9 , 4 , 5 , 3 ]

array.sort()
subsequence = []

subseq = [ array [ 0 ] ]
max_consec_length = 1
ans_index = 0

for index in range ( 1 , len ( array ) ) : 
    
    if array [ index - 1 ] + 1 == array [ index ] :
        subseq .append ( array [ index ] )
        
    else :
        subsequence .append ( subseq )
        
        if len ( subseq ) > max_consec_length :
            max_consec_length = len ( subseq )
            ans_index = len ( subsequence ) - 1
            
        subseq = []
        subseq .append ( array [ index ] )

print ( subsequence [ ans_index ] )
