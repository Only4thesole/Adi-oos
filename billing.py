import csv
import main

class Billing(object):
    self.active_profiles = []
    self.active_sizes = []

    def active_profile_add(self):
        profile_to_add = raw_input("Profile: ")
        size_to_add = raw_input("Size: ")
        add_size = self.active_sizes.append(size_to_add)
        with open("C:/Users/Nick/Desktop/nickbot/billing-accounts.csv", "rb") as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if self.billing_account == row[0]:
                    add_profile = self.active_profiles.append(profile_to_add)
                    print "Profile - {} Has Been Successfully Added to the Queue!".format(profile_to_add)
                    CLI().checkout_profile_menu()
                else:
                    print "This Profile Does NOT Exist..."
                    Billing().active_profile_add()
        self.profile = profile_to_add
        self.size = size_to_add

    def remove_profile(self):
        profile_to_remove = raw_input("Profile: ")
        if profile_to_remove in self.active_profiles:
            place = self.active_profiles.index(profile_to_remove)
            self.active_profiles.remove(profile_to_remove)
            del self.active_sizes[place]
            print "Profile - {} Has Been Successfully Removed from the Queue!".format(profile_to_remove)
            CLI().checkout_profile_menu()
        else:
            print "This Profile is Not Active or Does Not Exist"
            print "Please Try Again"
            Billing().remove_profile()

    def clear_list(self):
        del self.active_profiles[:]
        del self.active_sizes[:]
        print "All Profiles Have Been Successfully Removed!"
        CLI().checkout_profile_menu()

    def get_info(self):
        with open("C:/Users/Nick/Desktop/nickbot/billing-accounts.csv", "rb") as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if self.billing_account == row[0]:
                    try:
                        j = ",".join(str(e) for e in row)
                        w = j.replace(",,", ",N/A,")
                        self.first_name = str(w).split(",")[1]
                        self.last_name = str(w).split(",")[2]
                        self.street1 = str(w).split(",")[3]
                        self.street2 = str(w).split(",")[4]
                        self.city = str(w).split(",")[5]
                        self.state = str(w).split(",")[6]
                        self.phone = str(w).split(",")[7]
                        self.email = str(w).split(",")[8]
                        self.ccname = str(w).split(",")[9]
                        self.ccnumb = str(w).split(",")[10]
                        self.ccexp = str(w).split(",")[11]
                        self.ccv = str(w).split(",")[12]
                        self.cctype = str(w).split(",")[13]
                        self.card_type = self.cctype
                        if self.cctype=="VISA":
                            self.card_type = ("001")
                        elif self.cctype=="Master Card":
                            self.card_type = ("002")
                        elif self.cctype=="AMEX":
                            self.card_type = ("003")
                        elif self.cctype=="Discover":
                            self.card_type = ("004")
                        self.login_email = str(w).split(",")[14]
                        self.login_password = str(w).split(",")[15]
                    except IndexError:
                        login = False
                    else:
                        login = True
                    if profile_to_search != row[0]:
                        print "This Profile Does Not Exist!"
                        Billing.get_info()
