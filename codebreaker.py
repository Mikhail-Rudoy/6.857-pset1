ctxts = [[32, 14, 162, 166, 143, 97, 199, 84, 128, 186, 67, 246, 43, 37, 76, 222, 75, 131, 131, 185, 79, 149, 100, 201, 116, 219, 101, 188, 112, 206, 25, 63, 147, 142, 153, 112, 190, 67, 231, 37, 246, 85, 249, 123, 161, 135, 215, 124, 193, 143, 135, 201, 67, 237, 54, 246, 74, 196, 77, 80], [39, 0, 27, 44, 224, 51, 18, 23, 10, 43, 233, 81, 198, 215, 123, 142, 182, 124, 137, 167, 108, 187, 67, 244, 104, 192, 128, 151, 142, 174, 124, 225, 32, 250, 13, 90, 212, 35, 82, 206, 41, 3, 33, 236, 84, 242, 7, 60, 0, 21, 20, 36, 167, 143, 136, 201, 104, 164, 119, 218], [36, 10, 29, 37, 8, 28, 68, 254, 37, 16, 233, 93, 197, 133, 236, 29, 5, 36, 253, 57, 138, 216, 26, 34, 58, 82, 169, 192, 66, 8, 22, 123, 140, 135, 140, 137, 158, 96, 200, 64, 219, 111, 217, 82, 252, 100, 164, 158, 186, 155, 108, 193, 75, 254, 38, 167, 159, 105, 184, 157], [35, 6, 19, 53, 170, 127, 168, 114, 203, 116, 131, 188, 100, 181, 139, 153, 140, 136, 220, 78, 218, 52, 196, 114, 170, 203, 159, 246, 47, 18, 17, 56, 201, 64, 207, 94, 214, 43, 19, 9, 250, 30, 9, 5, 114, 206, 86, 251, 18, 52, 239, 77, 144, 180, 121, 163, 151, 141, 146, 164], [58, 204, 20, 103, 216, 44, 2, 14, 54, 235, 45, 25, 9, 26, 42, 234, 67, 249, 8, 36, 250, 19, 164, 143, 140, 237, 80, 245, 55, 27, 227, 75, 203, 20, 236, 60, 233, 45, 19, 15, 226, 6, 59, 248, 55, 9, 16, 59, 23, 63, 135, 205, 66, 230, 75, 197, 109, 170, 126, 143], [57, 205, 18, 17, 70, 214, 112, 183, 108, 207, 47, 29, 20, 33, 72, 204, 51, 232, 51, 236, 45, 246, 19, 3, 35, 13, 47, 8, 75, 247, 13, 114, 130, 142, 138, 146, 159, 127, 190, 8, 227, 7, 39, 236, 78, 182, 69, 255, 79, 244, 40, 49, 243, 72, 254, 47, 27, 20, 231, 56], [51, 23, 237, 70, 242, 6, 99, 132, 181, 111, 141, 177, 100, 251, 98, 162, 154, 134, 155, 139, 144, 159, 99, 210, 67, 247, 10, 32, 163, 168, 123, 161, 103, 181, 71, 148, 134, 146, 130, 158, 125, 181, 215, 77, 242, 91, 191, 39, 61, 19, 21, 107, 172, 150, 205, 91, 236, 43, 255, 16], [39, 7, 25, 32, 28, 238, 27, 239, 94, 213, 103, 213, 91, 245, 76, 197, 99, 220, 34, 17, 242, 48, 216, 15, 17, 55, 12, 38, 251, 64, 139, 164, 119, 192, 79, 156, 158, 125, 181, 111, 157, 142, 183, 107, 217, 81, 169, 152, 172, 193, 90, 233, 63, 242, 44, 224, 4, 20, 225, 99], [35, 6, 31, 114, 172, 120, 185, 81, 189, 126, 131, 183, 111, 128, 179, 119, 158, 133, 144, 185, 68, 138, 143, 142, 135, 232, 120, 202, 95, 227, 39, 10, 23, 227, 48, 233, 47, 211, 2, 4, 31, 7, 105, 169, 147, 190, 64, 168, 172, 149, 146, 164, 98, 199, 62, 249, 79, 222, 35, 116], [32, 14, 162, 189, 125, 158, 131, 204, 108, 210, 45, 15, 67, 29, 10, 28, 19, 2, 4, 55, 219, 97, 189, 96, 220, 120, 217, 99, 230, 106, 186, 223, 36, 226, 34, 228, 101, 191, 96, 234, 16, 60, 23, 10, 119, 217, 40, 3, 89, 231, 33, 54, 237, 93, 218, 92, 128, 132, 157, 171]]

answer = [[None for i in range(len(ctxts[0]))] for i in range(len(ctxts))]
archived_answers = {}

def print_answer(arg = None):
    if arg:
        a = archived_answers[arg]
    else:
        a = answer
    for l in a:
        s = ""
        for c in l:
            if c == None:
                s+="?"
            else:
                s+=c
        print s

def archive(val):
    archived_answers[val] = [l[:] for l in answer]

def restore(val):
    global answer
    archive("undo")
    answer = [l[:] for l in archived_answers[val]]

archive("restart")

def look_for_text(txt):
    global answer
    original = answer
    for i in range(len(ctxts[0]) - len(txt) + 1):
        for m in range(len(ctxts)):
            valid = True
            useful = False
            answer_copy = [l[:] for l in answer]
            for j in range(len(txt)):
                if answer_copy[m][i+j] == None:
                    useful = True
                if answer_copy[m][i+j] != None and answer_copy[m][i+j] != txt[j]:
                    valid = False
                answer_copy[m][i+j] = txt[j]
            if not valid or not useful:
                continue
            vals = [ctxts[m][i + j] ^ ord(txt[j]) for j in range(len(txt))]
            padpart = []
            for j in range(len(txt)):
                if i+j == 0:
                    padpart.append(vals[j])
                else:
                    padpart.append((vals[j] + 256 - ctxts[m][i+j-1])%256)
            s = ""
            valid = True
            for otherm in range(len(ctxts)):
                if otherm != m:
                    for j in range(len(txt)):
                        if i+j == 0:
                            c = padpart[j] ^ ctxts[otherm][i+j]
                        else:
                            c = ((padpart[j] + ctxts[otherm][i+j-1])%256) ^ ctxts[otherm][i+j]
                        valid = valid and (c < 128)
                        if answer_copy[otherm][i+j] != None and ord(answer_copy[otherm][i+j]) != c:
                            valid = False
                        answer_copy[otherm][i+j] = unichr(c)
            if valid:
                for l in answer_copy:
                    s = ""
                    for c in l:
                        if c == None:
                            s+="?"
                        else:
                            s+=c
                    print s
                if raw_input() in ["yes", "y"]:
                    answer = answer_copy
    if original != answer:
        archived_answers["undo"] = original

def Help():
    print """use the following commands to crack the code:
Help() to get help
print_answer() to print what you currently think the messages look like
archive(arg) to save your current guess under the key arg
restore(arg) to restore a previous level of knowledge (i.e. if you mess up)
print_answer(arg) to print what a particular saved guess looks like
look_for_text(txt) to guess part of the message and see where it could fit
 - enter y or yes to accept a potential location of the guessed message text
 - enter anything else to reject

the archive comes preset with a zero-knowledge setup saved under "restart", so you can use restore("restart") to restart"""

Help()
