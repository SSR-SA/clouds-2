import time
from locust import HttpUser, task, between

# class QuickstartUser (HttpUser):
#     @task
#     def hello_world(self):
#         self.client.get ("/numericalintegration/0/3.14159")


class QuickstartUser(HttpUser):
    host = "http://127.0.0.1:5000"

    @task
    def hello_world(self):
        self.client.get("/numericalintegration/0/3.14159")


az vmss create \
--resource-group scaleSet \
--name element2 \
--image UbuntuLTS \
--admin-username saiveera \
--generate-ssh-keys \
--instance-count 2 \
--vm-sku Standard_B1ms \
--upgrade-policy-mode automatic \
--lb-sku standard \
--location westeurope




az appservice plan create \
--name saiwbappplan1 \
--resource-group webapp \
--sku s1


az webapp create \
--name saiwbapp1 \
--resource-group saiwbapp1 \
--plan basicb1 \
--deployment-local-git











curl -X POST \
    -H 'Content-Type: application/zip' \
    -u 'webappcontainer3' \           
    -T <zip-file-name> \
    https://webappcontainer3.scm.azurewebsites.net/api/zipdeploy