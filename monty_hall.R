doors=c('A','B','C')
x=c()
for(i in 1:1000){
  car=sample(doors)[1] #fix a car
  pick=sample(doors)[1]  # start game
  pick1=sample(doors[which(doors!=pick & doors !=car)])[1]
  s_yes=doors[which(doors!=pick & doors!=pick1)]
  if(pick==car){
    x=append(x,0)
  }
  if(car==s_yes){
    x=append(x,1)
  }
}
countyes=0
countno=0
countyes=length(which(x==1))
countno=length(which(x==0))
print(countyes/length(x))
print(countno/length(x))