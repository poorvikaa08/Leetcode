int countDigits(int num) {
    int digit,count,x;

    x=num;
    count=0;

    while(num>0)
    {
        digit= num%10;
        if((x%digit)==0){
            count++;
        }
        num/=10;
    }

    return count;
    
}