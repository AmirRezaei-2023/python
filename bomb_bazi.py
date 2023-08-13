n,m =map(int,input().split())
k =int(input())

lis=[]
for i in range(k):
    row, col=map(int, input().split())
    lis.append([row, col])
##############################
def filler(n,m,lis):
    playground= [['#' for i in range(m)] for j in range(n)]
    for loc in lis:
        playground[loc[0]-1][loc[1]-1]= '*'
    return playground
########################################
def show_better(matrix):
    for row in matrix:
        str_row=''
        for col in row:
            str_row += col+ ' '
        print(str_row)

######################################
def counting(n,m,playground):
    for i in range(n):
        for j in range(m):
            if playground[i][j]=='#':
                sum_count=0
                try:
                    if playground[i][j-1]=='*' and not j==0 : sum_count+=1
                except: pass
                try:
                    if playground[i][j+1]=='*' : sum_count+=1
                except: pass
                try:
                    if playground[i-1][j]=='*' and not i==0 : sum_count+=1
                except: pass
                try:
                    if playground[i+1][j]=='*' : sum_count+=1
                except: pass
                try:
                    if playground[i-1][j-1]=='*' and not j==0 and not i==0: sum_count+=1
                except: pass
                try:
                    if playground[i-1][j+1]=='*' and not i==0 : sum_count+=1
                except: pass
                try:
                    if playground[i+1][j-1]=='*' and not j==0 : sum_count+=1
                except: pass
                try:
                    if playground[i+1][j+1]=='*'  : sum_count+=1
                except: pass
                playground[i][j]=str(sum_count)
    show_better(playground)
######################################
playground= filler(n,m,lis)
#show_better(playground)
counting(n,m,playground)
