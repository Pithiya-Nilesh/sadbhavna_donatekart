<template>

    <main class="profile-page" v-if="user_data">
        <section class="relative block h-500-px bg-blueGray-200">
            <Navbar />
            <!-- <div class="absolute top-0 w-full h-full bg-center bg-cover bg-black" style="background-image: url(''); ">
                <span id="blackOverlay" class="w-full h-full absolute opacity-0 bg-black"></span>
            </div>
            <div class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px"
                style="transform: translateZ(0);">
                <svg class="absolute bottom-0 overflow-hidden" xmlns="http://www.w3.org/2000/svg"
                    preserveAspectRatio="none" version="1.1" viewBox="0 0 2560 100" x="0" y="0">
                    <polygon class="text-blueGray-200 fill-current" points="2560 0 2560 100 0 100"></polygon>
                </svg>
            </div> -->
        </section>
        <section class="relative py-16 bg-blueGray-200">
            <div class="container mx-auto px-4">
                <!-- {{ user_data }} -->
                <!-- {{ user_data['user_type'] }} -->
                <div
                    class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64">
                    <div class="px-6">
                        <div class="flex flex-wrap justify-center">
                            <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                                <div v-if="user_data.data.user_image" class="relative">
                                    <img :src="user_data.data.user_image"
                                        class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                                    <!-- <Avatar :imageURL="http://sadbhavnadonatekart.com:8080/files/students.svguser_data.user_image" label="Felix" size="lg" /> -->
                                </div>
                                <div v-else class="relative">
                                    <div
                                        class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px">
                                    </div>
                                </div>
                            </div>
                            <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                                <div class="py-6 px-3 mt-32 sm:mt-0">
                                    <!-- <button
                                        class="bg-green-500  uppercase text-white font-bold hover:bg-green-500 hover:bg-white hover:text-green-500 hover:outline hover:outline-1 hover:outline-offset-1 shadow text-xs px-4 py-2 rounded  sm:mr-2 mb-1 ease-linear transition-all duration-150"
                                        type="button">
                                        Connect
                                    </button> -->
                                </div>
                            </div>
                            <div class="w-full lg:w-4/12 px-4 lg:order-1">
                                <div class="flex justify-center py-4 lg:pt-4 pt-8">
                                    <!-- <div class="mr-4 p-3 text-center">
                                        <span class="text-xl font-bold block uppercase tracking-wide text-blueGray-600">
                                            22
                                        </span>
                                        <span class="text-sm text-blueGray-400">Total Donation</span>
                                    </div>
                                    <div class="mr-4 p-3 text-center">
                                        <span class="text-xl font-bold block uppercase tracking-wide text-blueGray-600">
                                            10
                                        </span>
                                        <span class="text-sm text-blueGray-400">Photos</span>
                                    </div>
                                    <div class="lg:mr-4 p-3 text-center">
                                        <span class="text-xl font-bold block uppercase tracking-wide text-blueGray-600">
                                            89
                                        </span>
                                        <span class="text-sm text-blueGray-400">Comments</span>
                                    </div> -->
                                </div>
                            </div>
                        </div>
                        <div class="mt-12">
                            <div class="container mx-auto h-full">
                                <div class="w-full sm:pt-0 md:pt-5 lg:pt-12 bg-grey-lightest">
                                    <div class="container mx-auto py-0">
                                        <div class="w-4/6 lg:w:4/6 mx-auto bg-white">
                                            <!-- <div class="py-8 px-10 text-gray-600 text-black text-base text-4xl">Register & Login
                    </div> -->
                                            <div class="py-4 px-8">
                                                <!-- <div class="mb-4">
                                                    <label class="block text-gray-600 mb-2" for="email">First Name</label>
                                                    <input
                                                        class="appearance-none border-gray-300 rounded w-full py-2 px-3 text-grey-darker"
                                                        v-model="first_name" type="text">
                                                </div>
                                                <div class="mb-4">
                                                    <label class="block text-gray-600 mb-2" for="email">Last Name</label>
                                                    <input
                                                        class="appearance-none border-gray-300 rounded w-full py-2 px-3 text-grey-darker"
                                                        v-model="last_name" type="text">
                                                </div> -->
                                                <!-- <div class="mb-4">
                                                    <label class="block text-gray-600 mb-2" for="email">Full Name</label>
                                                    <input
                                                        class="appearance-none border-gray-300 rounded w-full py-2 px-3 text-grey-darker"
                                                        v-model="user_data.data.full_name" type="text">
                                                </div>
                                                <div class="mb-4">
                                                    <label class="block text-gray-600 text-base  mb-2"
                                                        for="email">Phone</label>
                                                    <input
                                                        class="appearance-none border-gray-300 rounded w-full py-2 px-3 text-grey-darker"
                                                        v-model="user_data.data.phone" type="text">
                                                </div>
                                                <div class="mb-4">
                                                    <label class="block text-gray-600 text-base  mb-2"
                                                        for="email">Email</label>
                                                    <input
                                                        class="appearance-none border-gray-300 rounded w-full py-2 px-3 text-grey-darker"
                                                         :value="user_data.data.email" type="text">
                                                </div> -->
                                                <!-- <div class="mb-4">
                                                    <label class="block text-gray-600 text-base  mb-2" for="email">PAN
                                                        Details</label>
                                                    <input
                                                        class="appearance-none border-gray-300 rounded w-full py-2 px-3 text-grey-darker"
                                                        v-model="pan_details" type="text">
                                                </div> -->
                                                <!-- <div class="mb-4">
                                                    <button
                                                        class="appearance-none border-gray-600 rounded w-full py-2 px-3 text-grey-darker bg-green-500 hover:bg-transparent text-white hover:text-green-500 py-2 tracking-wide px-4 border border-green-500 hover:border-green-500 py-3 text-xs uppercase rounded"
                                                        @click="update()">Update</button>
                                                </div> -->

                                                <!-- ******************************************* -->

                                                <div class="text-center">
                                                    <h3
                                                        class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                                                        {{ user_data.data.full_name }}
                                                    </h3>
                                                    <div
                                                        class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                                                        <div>{{ user_data.data.email }}</div>
                                                        <div>{{ user_data.data.phone }}</div>
                                                    </div>
                                                    <!-- <div class="mb-2 text-blueGray-600 mt-10">
                                                        <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                                                        Solution Manager - Creative Tim Officer
                                                    </div>
                                                    <div class="mb-2 text-blueGray-600">
                                                        <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                                                        University of Computer Science
                                                    </div> -->
                                                </div>

                                                <!-- ******************************************* -->


                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- <div class="mt-10 py-10 border-t border-blueGray-200 text-center">
                            <div class="flex flex-wrap justify-center">
                                <div class="w-full lg:w-9/12 px-4">
                                    <p class="mb-4 text-lg leading-relaxed text-blueGray-700">
                                        An artist of considerable range, Jenna the name taken by
                                        Melbourne-raised, Brooklyn-based Nick Murphy writes,
                                        performs and records all of his own music, giving it a
                                        warm, intimate feel with a solid groove structure. An
                                        artist of considerable range.
                                    </p>
                                    <a href="javascript:void(0)" class="font-normal text-emerald-500">
                                        Show more
                                    </a>
                                </div>
                            </div>
                        </div> -->

                        <div v-if="donation_details.data != ''" class="text-center text-2xl text-gray-600">Your Donations</div>
                        <div v-if="donation_details.data != ''" class="flex flex-col">
                            <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
                                <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
                                    <div class="overflow-hidden">
                                        <table class="min-w-full">
                                            <thead class="bg-white border-b">
                                                <tr>
                                                    <th scope="col"
                                                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                                        Campaign Name
                                                    </th>
                                                    <th scope="col"
                                                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                                        Amount
                                                    </th>
                                                    <th scope="col"
                                                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                                        Date
                                                    </th>
                                                    <th scope="col"
                                                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                                        Mode of Payment
                                                    </th>
                                                    <th scope="col"
                                                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                                                        Download 80G Certificate
                                                    </th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr v-for="donation in donation_details.data"
                                                    class="bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100">
                                                    <td
                                                        class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                                        {{ donation.name }}</td>
                                                    <td
                                                        class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                                        {{ donation.amount }}</td>
                                                    <td
                                                        class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                                        {{ donation.date }}</td>
                                                    <td
                                                        class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                                                        {{ donation.mode_of_payment }}</td>
                                                    <td
                                                        class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                                                        @click="download_80g(donation.name, donation.date)">
                                                        Download</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div v-else>
                        <div class="text-center font-bold text-gray-500"> Donate Item to see Donations and Download Certificate </div>    
                        <div class="text-center text-sm leading-normal mt-2 mb-5 text-blue-400 font-bold"><router-link to="/home">Click Here To Show Campaign</router-link></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <Footer />
</template>
<script>
import Navbar from "../../components/Navbar.vue";
import Footer from "../../components/Footer.vue";
import { Avatar } from 'frappe-ui'
import { useRoute } from 'vue-router';
import axios from "axios";

export default {
    name: "Login",
    components: { Navbar, Footer },
    data() {
        return {
            user_data: '',
            donation_details: '',
            donor: ''
        }
    },
    mounted() {
        const name = useRoute();
        this.get_user_detail(name.params.name)
        this.get_donation_details(name.params.name)
        this.donor = name.params.name
    },
    resources: {
        download_80g(){
            return{
                method: 'sadbhavna_donatekart.api.donor.download_80g',
                onSuccess:(res) => {
                    console.log("okey", res)
                    let url = `/api/method/frappe.utils.print_format.download_pdf?doctype=Tax Exemption 80G Certificate&name=${res}&format=80G Certificate for Donation`
                    window.location = url;
                },
                onError: (error) => {
                    console.log("somthing want wrong!", error)
                }

            }
        }
    },
    methods: {
        get_user_detail(name) {
            let url = "/api/resource/User/" + name
            fetch(url, {
                method: 'GET',
            })
                .then(response => {
                    response.json().then(res => {
                        // console.log("asdf", res)
                        this.user_data = res
                    });
                })
                .catch(err => {
                    console.error(err);
                });
        },
        get_donation_details(name) {
            let url = `/api/resource/Donation?filters={"email": "${name}"}&fields=["*"]`
            fetch(url, {
                method: 'GET'
            }).then(response => {
                response.json().then(res => {
                    // console.log("campaign", res)
                    this.donation_details = res
                });
            }).catch(error => {
                console.log(error);
            })
        },
        download_80g(donation, date){
            this.$resources.download_80g.submit({
                donation: donation,
                date: date,
                donor: this.donor
            })
        }
    }
}
</script>