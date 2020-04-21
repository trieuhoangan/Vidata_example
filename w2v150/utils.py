class Dataload:
    def __init__(self,link_file,mode):
        self.w2v = self.load_150_vec(link_file,mode)

    def load_150_vec(self,link_file,mode_output):
        all_data =[]
        # try:
        with open(link_file,'r',encoding='utf-8') as reader:
            all_data = reader.readlines()
        print(len(all_data))
        if mode_output == 0:
            w2v_model = {}
            for i in range(2,len(all_data)):
                try:
                    row = all_data[i].replace('\n','')
                    parts_of_line = row.split(' ')
                    count = 0
                    vector = []
                    key = parts_of_line[0]
                    for j in range(2,len(parts_of_line)-1):
                        try:
                            vector.append(float(parts_of_line[j]))
                        except ValueError:
                            print("error at row {} dimension {}".format(i,j))
                        except TypeError:
                            print("type error at row {} dimension {}".format(i,j))
                    w2v_model[key]=vector
                except:
                    print("type error at row {}".format(i))
            return w2v_model
        else:
            key_word = []
            vectors = []
            for i in range(2,len(all_data)):
                parts_of_line = all_data[i].split(' ')
                count = 0
                vector = []
                for part in parts_of_line:
                    if count == 0:
                        key_word.append(part)
                        count = count + 1
                    else:
                        vector.append(part)
                vectors.append(vector)
            w2v_model=(key_word,vectors)
            return w2v_model
    
if __name__ == "__main__":
    link_150 = '../ViData/W2V_150.txt'
    # load_150_vec(link_150,0)