class AccessMixin(object):
    # check that a page has the proper access
    def staff_required(self, url, text=None):
        """ Run through permission tests that require staff. 
            Sometimes we'll pass in a string and check the response 
            for that string
        """
        anon_response = self.app.get(url)
        self.assertEqual(anon_response.status_code, 302)

        user_response = self.app.get(url, user=self.user)
        self.assertNotEqual(anon_response.status_code, 200)     
        
        staff_response = self.app.get(url, user=self.staff_user)
        self.assertEqual(staff_response.status_code, 200)

    def login_required(self, url):
        """ test login required views and forms
        """
        response = self.app.get(url)
        self.assertEqual(response.status_code, 302)

        response = self.app.get(url, user=self.user)
        self.assertEqual(response.status_code, 200)

    def real_estate_access(self, url, text):
        """ test that the real estate users are the only non-admin users
            that can access their real estate information
        """
        user_response = self.app.get(url, user=self.user)
        assert self.access_denied_message in user_response

        re_response = self.app.get(url, user=self.real_estate_user)
        assert text in re_response


