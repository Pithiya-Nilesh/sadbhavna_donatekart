<template>
  <Navbar />
  <div class="container mx-auto h-full my-20">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-full lg:w-4/12 px-4">
        <div class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
          <div class="flex-auto px-4 lg:px-10 py-10 pt-5">
            <div class="text-blueGray-400 text-center mb-3 font-bold text-xl">
              <small>sign in </small>
            </div>
            <form>
              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlFor="grid-password">
                  Email
                </label>
                <input v-model="email" type="email"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Email" required />
              </div>

              <div class="relative w-full mb-3">
                <label class="block uppercase text-blueGray-600 text-xs font-bold mb-2" htmlFor="grid-password">
                  Password
                </label>
                <input v-model="password" type="password"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Password" required />
              </div>
              <div class="text-center mt-6">
                <button style="background-color: #40b751;"
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-4 w-full ease-linear transition-all duration-150"
                  type="button" @click="login()">
                  Sign In
                </button>
              </div>
              <router-link to="/sadbhavna/registration" class="text-green-500">Register</router-link>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!-- <GoogleLogin :callback="login_with_google">
        </GoogleLogin>

        <button @click="login_with_google1">Login With Google</button>
        <div>{{ isLogin }}</div> -->



  </div>


  <div class="container mx-auto h-full">
    <div class="w-full pt-0 md:pt-5 lg:pt-12 bg-grey-lightest">
      <div class="container mx-auto py-0">
        <div class="w-4/6 lg:w:4/6 mx-auto bg-white">
          <div class="py-8 px-10 text-gray-600 text-black text-center text-4xl">Register & Login
          </div>
          <div class="py-4 px-8">
            <div class="mb-4">
              <label class="block text-gray-600 text-base  mb-2" for="email">Enter WhatsApp Number</label>
              <input class="appearance-none border-gray-600 rounded w-full py-2 px-3 text-grey-darker" v-model="email"
                type="number">
              <span class="text-sm text-gray-400"> An OTP will be sent to this whats app number</span>
            </div>
            <div class="mb-4">
              <button
                class="appearance-none border-gray-600 rounded w-full py-2 px-3 text-grey-darker bg-green-500 hover:bg-transparent text-white hover:text-green-500 py-2 tracking-wide px-4 border border-green-500 hover:border-green-500 py-3 text-xs uppercase rounded">Login
                with Whatsapp</button>
            </div>
            <div class="mb-4">
              <div
                class="flex items-center uppercase text-gray-600 my-4 before:flex-1 before:border-t before:border-gray-600 before:mt-0.5 after:flex-1 after:border-t after:border-gray-600 after:mt-0.5">
                <p class="text-center mx-4 mb-0">Or</p>
              </div>
            </div>
            <div class="mb-4">
              <button
                class="appearance-none border-gray-600 rounded w-full py-2 px-3 text-grey-darker bg-green-500 hover:bg-transparent text-white hover:text-green-500 py-2 tracking-wide px-4 border border-green-500 hover:border-green-500 py-3 text-xs uppercase rounded">Login
                with SMS</button>
            </div>
            <div class="mb-4">
              <button
                class="appearance-none border-gray-600 rounded w-full py-2 px-3 text-grey-darker bg-green-500 hover:bg-transparent text-white hover:text-green-500 py-2 tracking-wide px-4 border border-green-500 hover:border-green-500 py-3 text-xs uppercase rounded">Login
                with Email</button>
            </div>
            <div class="mb-4">
              <button
                class="appearance-none border-gray-600 rounded w-full py-2 px-3 text-grey-darker bg-green-500 hover:bg-transparent text-white hover:text-green-500 py-2 tracking-wide px-4 border border-green-500 hover:border-green-500 py-3 text-xs uppercase rounded">Login
                with Facebook</button>
            </div>
            <GoogleLogin :callback="login_with_google" class="w-full">
              <div class="mb-4">
                <button
                  class="appearance-none border-gray-600 rounded w-full py-2 px-3 text-grey-darker bg-green-500 hover:bg-transparent text-white hover:text-green-500 py-2 tracking-wide px-4 border border-green-500 hover:border-green-500 py-3 text-xs uppercase rounded">Login
                  with Google</button>
              </div>
            </GoogleLogin>
            <div class="mb-4">
              <div class="flex mb-10 justify-between">
                <span class="text-gray-600">Forget password? <a class="text-green-500" href="/login.html">Click
                    here</a></span><a class="text-green-500" href="registration.html">Register</a>
              </div>
            </div>
            <div class="mb-4">
              <span class="block text-gray-600 text-center text-base  mb-2"><a class="text-green-500"
                  href="registration.html">Login </a> &nbsp;via ID Password</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>






<Footer />
</template>

<script>
// import github from "@/assets/Inter/img/github.svg";
// import google from "@/assets/Inter/img/google.svg";
import { decodeCredential } from 'vue3-google-login'

import Navbar from "../../components/Navbar.vue";
import Footer from "../../components/Footer.vue";


export default {
  name: "Login",
  components: { Navbar, Footer },
  data() {
    return {
      // github,
      // google,
      password: "",
      email: "",
      isLogin: false
    };
  },
  resources: {
    login() {
      return {
        method: "/api/method/login",
        // method: '/api/method/frappe.integrations.oauth2.get_token',
        onSuccess: async () => {
          this.$router.push(`/home`);
        },
        onError: (error) => {
          alert("Invalid Login");
          this.email = "";
          this.password = "";
        },
      };
    },
    login_with_google() {
      return {
        method: 'frappe.www.login.login_via_token',
        onSuccess: () => {
          console.log("okey")
        },
        onError: (error) => {
          console.log("error", error)
        }
      }
    },
    // googleAuthCodeLogin(){
    //   return{
    //     method: '/sadbhavna_donatekart.api.api.login_with_google',
    //     onSuccess: () => {
    //       console.log("okey")
    //     },
    //     onError: (error) => {
    //       console.log("error", error)
    //     }
    //   }
    // }
  },
  methods: {
    login() {
      this.$resources.login.submit({
        usr: this.email,
        pwd: this.password,
      });
      // axios.get('/api/method/login', {
      //   params: {
      //     usr: this.email,
      //     pwd: this.password
      //   }
      // }).then(function (response){
      //   // console.log("response", response.data['home_page']);
      //   this.$router.push(`/home`)
      // }).catch(function (error){
      //   console.log(error);
      // })
      //   axios.post("/api/method/login",{
      //       usr: email,
      //       pwd: password
      //     }
      //   );
      //   this.$session.start();
      //   this.$session.set("jwt", token);
      //   console.log($session.get('jwt'))
    },


    // async login_with_google(){
    //   const googleUser = await this.$gAuth.signIn();
    //   console.log("Google User", googleUser)
    //   console.log("getId", googleUser.getId())
    // }

    // login_with_google(){
    //   window.location = 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?redirect_uri=http%3A%2F%2Fsadbhavnadonatekart.com%3A8000%2Fapi%2Fmethod%2Ffrappe.www.login.login_via_google&state=eyJzaXRlIjogImh0dHA6Ly9zYWRiaGF2bmFkb25hdGVrYXJ0LmNvbTo4MDAwIiwgInRva2VuIjogIjQ3ZDk5YzFmN2QzNTYwZWJhNGY0MzhiNWFiMjA2ZTlmYmM1ZjlkODA0NjIwZDJhZDhlYmIzMGMyIiwgInJlZGlyZWN0X3RvIjogbnVsbH0%3D&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&response_type=code&client_id=615226899593-b4jpeolmo526beqkiqvo1bf7ob06rhpb.apps.googleusercontent.com&service=lso&o2v=1&flowName=GeneralOAuthFlow'
    // }

    login_with_google: (response) => {
      console.log("data", response)
      let userData = decodeCredential(response.credential)
      let email = userData.email
      let first_name = userData.family_name
      let last_name = userData.given_name
      let image_url = userData.picture

      console.log("asdfads", userData)

      let url = `http://sadbhavnadonatekart.com:8080/api/method/sadbhavna_donatekart.api.api.login_with_google?email=${email}&first_name=${first_name}&last_name=${last_name}&image_url=${image_url}`
      fetch(url, {
        method: 'GET'
      })
        .then(response => {
          response.json().then(res => {
            console.log("asdf", res.message)
            console.log("asdf", res)
            let token = res.message
            // this.$router.push('/home')
            window.location = 'http://sadbhavnadonatekart.com:8080/home'
            // this.$resources.login_with_google.submit({
            //   login_token: token
            // })
            // fetch('http://sadbhavnadonatekart.com:8000/api/method/frappe.www.login.login_via_token', {
            //   headers: {
            //     'Authorization': `Bearer ${token}`
            //   }
            // })
            // let url1 = `http://sadbhavnadonatekart.com:8000/api/method/frappe.www.login.login_via_token?login_token=${token}`
            // fetch(url1)
            //   .then(r => r.json())
            //   .then(r => {
            //     console.log(r);
            //   })

          });
        })
        .catch(function (error) {
          log('Request failed', error)
        });

      // this.$resources.login_with_google.submit({
      //   user_data: response
      // })
    },
    // login_with_google1(){

    // }
  }
};
</script>


