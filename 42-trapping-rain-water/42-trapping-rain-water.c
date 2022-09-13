

int trap(int* height, int heightSize){
    int *p,*p1,i;
    unsigned int w=0;
    if(heightSize<3)
        return 0;
    p=(int*)malloc(sizeof(int)*heightSize);
    p1=(int*)malloc(sizeof(int)*heightSize);
    p[0]=height[0];
    for(i=1;i<heightSize;i++)
    {
        if(p[i-1]>height[i])
            p[i]=p[i-1];
        else
            p[i]=height[i];
//        printf("%d %d\n",p[i],height[i]);
    }
    p1[heightSize-1]=height[heightSize-1];
    for(i=heightSize-2;i>=0;i--)
    {
        if(p1[i+1]>height[i])
            p1[i]=p1[i+1];
        else
            p1[i]=height[i];
//        printf("%d %d\n",p1[i],height[i]);
    }
    i=1;
    while(i<heightSize)
    {
        if(p[i]>p1[i])
            w=w+p1[i]-height[i];
        else
            w=w+p[i]-height[i];
        i++;
    }
    return w;
    

}