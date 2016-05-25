from contact import *

contact_amanda = Contact("Amanda", "Nagai")
contact_amanda.twitter_handle = "amandanagai"
contact_victoria = Contact("Victoria", "Yau")
contact_victoria.email = "victoriayiyau@yahoo.com"
contact_lydia = Contact("Lydia", "Huang")

contacts_list = []
contacts_list.extend([contact_amanda, contact_victoria, contact_lydia])

contact_amanda.send_tweet("We're awesome!")

contact_victoria.send_email("We'll be home at 10pm.")