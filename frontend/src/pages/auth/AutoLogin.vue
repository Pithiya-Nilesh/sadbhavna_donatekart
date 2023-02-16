<template>
    <Navbar />
    <div class="container mx-auto h-full">
        <div class="w-full pt-0 md:pt-5 lg:pt-12 bg-grey-lightest">
            <div class="container mx-auto py-0">
                <div class="w-4/6 lg:w:4/6 mx-auto bg-white">
                    <div class="py-8 px-10 text-gray-600 text-black text-center text-4xl">Register & Login
                    </div>
                    <div class="py-4 px-8">
                        <div class="mb-4">
                            <label class="block text-gray-600 text-base  mb-2" for="email">Enter WhatsApp Number</label>
                            <input class="appearance-none border-gray-600 rounded w-full py-2 px-3 text-grey-darker"
                                v-model="email" type="number">
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
                        <!-- <div class="mb-4">
                            <div class="flex mb-10 justify-between">
                                <span class="text-gray-600">Forget password? <a class="text-green-500" href="http://sadbhavnadonatekart.com:8080/api/method/frappe.core.doctype.user.user.reset_password?">Click
                                    here</a></span><a class="text-green-500" href="/sadbhavna/registration">Register</a>
                            </div>
                            </div> -->
                        <div class="mb-4">
                            <span class="block text-gray-600 text-center text-base  mb-2"><router-link
                                    class="text-green-500" to="/sadbhavna/login">Login </router-link> &nbsp;via ID
                                Password</span>
                        </div>u
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
    name: "Auto Login",
    components: { Navbar, Footer },
    data() {
        return {
            // github,
            // google,
            // password: "",
            // email: "",
            // isLogin: false
        };
    },
    resources: {
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
    },
    methods: {
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
                    });
                })
                .catch(function (error) {
                    log('Request failed', error)
                });
        },
    }
};
</script>
  
  
  