<template>
    <Navbar />
    <div class="container mx-auto h-full">
        <!-- Content -->
        <div class="w-full bg-grey-lightest" style="padding-top: 4rem;">
            <div class="container mx-auto py-8">
                <div class="w-5/6 lg:w-1/2 mx-auto bg-white rounded shadow">
                    <div class="py-4 px-8 text-black text-xl">Donor Registration
                    </div>
                    <div class="py-4 px-8">
                        <div class="flex mb-4">
                            <div class="w-1/2 mr-1">
                                <label class="block text-grey-darker text-sm font-bold mb-2" for="first_name">First
                                    Name</label>
                                <input class="appearance-none border rounded w-full py-2 px-3 text-grey-darker"
                                    v-model="first_name" type="text" placeholder="Your first name" required>
                            </div>
                            <div class="w-1/2 ml-1">
                                <label class="block text-grey-darker text-sm font-bold mb-2" for="last_name">Last
                                    Name</label>
                                <input class="appearance-none border rounded w-full py-2 px-3 text-grey-darker"
                                    v-model="last_name" type="text" placeholder="Your last name" required>
                            </div>
                        </div>
                        <div class="mb-4">
                            <label class="block text-grey-darker text-sm font-bold mb-2" for="email">Email
                                Address</label>
                            <input class="appearance-none border rounded w-full py-2 px-3 text-grey-darker"
                                v-model="email" type="email" placeholder="Your email address" required>
                        </div>
                        <div class="mb-4">
                            <label class="block text-grey-darker text-sm font-bold mb-2" for="password">Password</label>
                            <input class="appearance-none border rounded w-full py-2 px-3 text-grey-darker"
                                v-model="password" type="password" placeholder="Your secure password" required>
                        </div>
                        <div class="mb-4">
                            <label class="block text-grey-darker text-sm font-bold mb-2" for="password">Confirm
                                Password</label>
                            <input class="appearance-none border rounded w-full py-2 px-3 text-grey-darker"
                                v-model="conform_password" type="password" placeholder="Your secure password" required>
                        </div>
                        <div class="mb-4">
                            <label class="block text-grey-darker text-sm font-bold mb-2" for="number">Phone
                                Number</label>
                            <input class="appearance-none border rounded w-full py-2 px-3 text-grey-darker"
                                v-model="phone_number" type="number" placeholder="Your phone number" required>
                        </div>
                        <div class="mb-4">
                            <label class="block text-grey-darker text-sm font-bold mb-2" for="pan number">Pan
                                Number</label>
                            <input class="appearance-none border rounded w-full py-2 px-3 text-grey-darker"
                                v-model="pan_number" type="text" placeholder="Your pan number" required>
                        </div>
                        <div class="flex items-center justify-between mt-8">
                            <button
                                class="bg-green-500 mb-2 uppercase hover:bg-blue-dark text-white py-2 px-8 rounded-lg"
                                type="submit" @click="register()">
                                Register
                            </button>
                        </div>
                        <router-link to="/sadbhavna/login">Already have an account? Sign In</router-link>
                        <!-- <a href="/sadbhavna/login">Already have an account? Sign In</a> -->

                        <!-- <p class="text-grey text-xs mt-1"></p> -->
                    </div>
                </div>
            </div>
        </div>
    </div>
    <Footer />
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import Footer from "../../components/Footer.vue";
export default {
    name: 'Registration',
    components: {
        Navbar,
        Footer
    },
    data() {
        return {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            conform_password: '',
            phone_number: '',
            pan_number: ''
        }
    },
    resources: {
        register() {
            return {
                method: 'sadbhavna_donatekart.api.api.register',
                onSuccess: (res) => {
                    // this.recent_donation = res
                    if (confirm("your registration is successfully now you can login") == true) {
                        this.$router.push(`/sadbhavna/login`)
                    } else {
                        this.$router.go(-1)          
                    }
                },
                onError: (error) => {
                    alert("Somthing want Wrong!", error)
                    console.log(error)
                }
            }
        }
    },
    methods: {
        register() {
            if (this.password == this.conform_password) {
                this.$resources.register.submit({
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    password: this.password,
                    phone_number: this.phone_number,
                    pan_number: this.pan_number
                })
            }
            else {
                alert("Your password is not match")
                this.password = ''
                this.conform_password = ''
            }
        }
    }
}
</script>