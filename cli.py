import BruteForce
import Main

class CLI(object):
    def main_menu(self):
        print "1. Start Brute Forcer"
        print "2. Add Checkout Profiles"
        decision = raw_input("")
        if "1" in decision:
            BruteForce().start()
        elif "2" in decision:
            Main().checkout_profiles()

    def checkout_profile_menu(self):
        print ""
        print "==============================="
        print ""
        if self.checkout_profile_list == []:
            print "Active Billing Profiles: NONE"
        else:
            print "Active Billing Profiles: {}".format(self.checkout_profile_list)
        if self.size_list == []:
            print "Sizes: NONE"
        else:
            print "Sizes: {}".format(self.size_list)
        print "1. Add Profile"
        print "2. Remove Profile"
        print "3. Clear Profiles"
        print "4. Back"
        decision = raw_input("")
        if "1" in decision:
            Billing().active_profile_add()
        elif "2" in decision:
            Billing().remove_profile()
        elif "3" in decision:
            Billing().clear_list()
        elif "4" in decision:
            CLI().main_menu()
