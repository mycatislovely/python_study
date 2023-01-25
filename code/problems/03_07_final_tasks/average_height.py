
def height_statistics(input_file_name):            
    c = [[0] * 2 for i in range(12)]
    with open(input_file_name, 'r', encoding = 'UTF-8') as f: 
        for line in f:
            i, _, h = line.strip().split('\t')
            i = int(i)
            h = float(h)
            c[i][0] += 1
            c[i][1] += h
    return c    

def print_statistics(stats, output_file_name):
    with open(output_file_name, 'w', encoding = 'UTF-8') as f:
        for i in range(1, len(stats)): 
            n, h = stats[i]
            f.write(str(i) + ' ' + (str(h / n) if n > 0 else '-') + '\n')

    
stats = height_statistics('dataset_3380_5 (2).txt')   
print_statistics(stats, 'average_height_output.txt')
        


    
           
        
