<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-full lg:w-4/12 px-4">
        <div
          class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0"
        >
          <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
            <div class="text-blueGray-400 text-center mb-3 font-bold">
              <small>sign in </small>
            </div>
            <form>
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  Email
                </label>
                <input
                  v-model="email" type="email"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Email"
                  required
                />
              </div>

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  Password
                </label>
                <input
                  v-model="password"
                  type="password"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Password"
                  required
                />
              </div>
              <div class="text-center mt-6">
                <button
                style="background-color: #40b751;"
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                  type="button"
                  @click="login()"
                >
                  Sign In
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import github from "@/assets/Inter/img/github.svg";
import google from "@/assets/Inter/img/google.svg";

export default {
  name: "Login",
  data() {
    return {
      github,
      google,
      password: '',
      email: '',
    };
  },
  resources: {
    login() {
      return {
        method: "/api/method/login",
        // method: '/api/method/frappe.integrations.oauth2.get_token',
        onSuccess: async () => {
          this.$router.push(`/home`)
        },
        onError: (error) => {
					alert("Invalid Login")
          this.email = '';
          this.password = '';
				},
      }
    }
  },
  methods:{
    login(){
      this.$resources.login.submit({
          usr: this.email,
          pwd: this.password,
        })

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
      
    }
  }
};
</script>
