int numberOfEmployeesWhoMetTarget(int* hours, int hoursSize, int target){
    int i,num;
    num=0;
    for(i=0;i<hoursSize;i++){
        if(hours[i]>=target)
            num++;
    }
    return num;
}