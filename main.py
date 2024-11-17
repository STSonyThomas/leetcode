# int array
# filter elemtns for each element-> no element greater than curr element to right side
def main(array):
    input_array = array
    output_array=[]
    max_el=array[-1]
    for i in range(len(input_array)-1,-1,-1):
        # flag=True
        # for j in range(i+1,len(input_array)):
        #     if input_array[i]<input_array[j]:
        #         flag=False
        #         break
        # if flag:
        #     output_array.append(input_array[i])
        if input_array[i]>=max_el:
            max_el=input_array[i]
            output_array.append(max_el)
            
        # print(input_array[i])
    return output_array

if __name__ == "__main__":
    ex1=[4,1,1,8,9]
    op = main(ex1)
    print(op)
