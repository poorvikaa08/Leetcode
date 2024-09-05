int sumOfMultiples(int n){
    int i,sum;
    sum=0;
    for(i=1;i<=n;i++)
    {
        if(i%3==0)
            sum+=i;
        else if(i%5==0)
            sum+=i;
        else if(i%7==0)
            sum+=i;
    }
    return sum;
}