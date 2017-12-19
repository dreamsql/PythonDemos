import re




if __name__ == '__main__':
    path = r"D:\4. iExchange_V3.sql"
    content_pattern = 'CREATE\s+PROCEDURE\s+\[Trading\]\.\[SaveResetStatus\]'
    end_pattern = '^end$'
    content = []
    content_found = False
    end_found = False
    with open(path, encoding = 'utf-8') as f:
        for line in f:
            if re.search(content_pattern, line,re.IGNORECASE):
                print(line)
                content_found = True
            if content_found and re.match(end_pattern,line, re.IGNORECASE):
                end_found = True
                content.append(line)
                break
            if content_found and not end_found:
                content.append(line)
    
    if len(content) > 0:
        print("have")
        with open(r'D:\Programming\python\work\sqlData.txt', 'w',encoding = 'utf-8') as f:
            for line in content:
                f.write(line)
    
                
                




