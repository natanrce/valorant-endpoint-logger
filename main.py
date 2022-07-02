import os
import re

def process_data(data):
    request_regex = 'QueryName: \[(.+?)], URL \[(\w+?) (.+?)], TraceID: \[.+?] Response Code: \[(\d+)]'

    keys = [
        'name',
        'method',
        'url',
        'status_code'
    ]
    
    if request := re.search(request_regex, data):
        req_groups = request.groups()
        
        # Save the result to a dictionary
        result = dict(zip(keys, req_groups))
        
        url = result['url']
        name = result['name']
        method = result['method']
        status_code = result['status_code']
        
        print(f'[{name}] {method} {url} - {status_code}')

def main():
    log_path = os.path.join(
        os.getenv('LOCALAPPDATA'), 
        r'VALORANT\Saved\Logs\ShooterGame.log'
    )
    
    with open(log_path, 'r') as file:
        while True:
            line = file.readline()

            if "https://" in line:
                process_data(line)

if __name__ == '__main__':
    main()
