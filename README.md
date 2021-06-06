## How to:

### Before you start, please ensure `git` / `ansible` / `docker-compose` are installed.
##
### Running options:
- Clone the repo: ```git clone https://github.com/ctepx25/panaya.git /tmp/panaya/```
- Start environment:  ``` ansible-playbook /tmp/panaya/ansible.yaml ```  and type ```deploy```.
- Rebuild nginx server image:  ``` ansible-playbook /tmp/panaya/ansible.yaml ```  and type ```rebuild```. 
- Restart nginx server:  ``` ansible-playbook /tmp/panaya/ansible.yaml ```  and type ```restart```. 
- Terminate: ``` ansible-playbook /tmp/panaya/ansible.yaml ```  and type ```terminate```.

##
### Nice to have CI pipeline:
<img src="panaya-tag-flow.png" width="70%" height="70%"/>
