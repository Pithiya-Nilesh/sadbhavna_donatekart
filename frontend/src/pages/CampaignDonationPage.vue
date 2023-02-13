<template>
    <div class="top-0 w-full h-3/6 bg-center bg-right bg-transparent bg-cover"
        style="background-image: url('../../src/assets/Inter/img/explore-campaign.jpg'); ">

        <Navbar />
        <div class="container mx-auto grid sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-2">
            <p
                class="text-5xl mb-40 text-center md:text-center md:text-base lg:text-left pt-20 font-bold text-green-500 leading-11">
                <span class="text-gray-600"> Join hands with </span> Sadbhana Campaigns<span class="text-gray-600"> to
                    help needy.</span> </p>
        </div>

    </div>

    <div class="container mx-auto mt-20">
        <div v-if="campaign_detail">
            <!-- {{ campaign_detail }}  -->
            <h2 style="font-size: 2rem;" class="text-gray-600">{{ campaign_detail.data.campaign_title }}</h2>
            <p class="text-gray-500">{{ campaign_detail.data.short_description }}</p>

            <div class="flex flex-wrap mt-6 mb-5">
                <div class="w-full lg:w-8/12 pr-4">
                    <!-- <DonationDetail /> -->
                    <img class="object-fill w-full mb-4" :src="campaign_detail.data.campain_image">
                    <div class="w-full bg-gray-200 rounded-md dark:bg-gray-700">
                        <!-- <div class="bg-green-500 text-xs font-medium text-grren-100 text-center p-0.5 leading-none rounded-md" style="width: 40%"> 40%</div> -->
                        <div class="bg-green-500 text-xs font-medium text-grren-100 text-center p-0.5 leading-none rounded-md"
                            :style="{ width: campaign_detail.data.raised_amount * 100 / campaign_detail.data.donation_amount + '%' }">
                            {{ campaign_detail.data.raised_amount * 100 / campaign_detail.data.donation_amount }}%</div>
                    </div>
                    <div class="pt-4 pb-2 flex justify-between font-bold">
                        <p>Raised: {{ campaign_detail.data.raised_amount }}</p>
                        <p>Goal: {{ campaign_detail.data.donation_amount }}</p>
                    </div>
                    <!-- <pre> -->
                    <!-- <code> -->
                    <p class="text-gray-500">
                        {{ campaign_detail.data.about_campaign }}
                    </p>
                    <!-- </code> -->
                    <!-- </pre> -->


                </div>
                <div class="w-full lg:w-4/12 pl-4">
                    <!-- <DonationDetailRightside /> -->
                    <div style="font-size: 2rem;" class="text-gray-600">Product</div>
                    <div v-for="products in campaign_detail.data.add_campaign_items">
                        <!-- {{ products }} -->
                        <div class="block rounded-lg shadow-lg bg-white pl-5">
                            <div class="flex flex-wrap items-center pt-10">
                                <div class="lg:flex lg:w-3/12 xl:w-3/12">
                                    <img :src="products.image" :alt="products.display_as_name"
                                        class="rounded-full w-30 h-20" />
                                </div>
                                <div class="lg:w-9/12 xl:w-9/12">
                                    <div class="md:px-12">
                                        <h4 class="text-xl text-green-500">{{ products.display_as_name }}</h4>
                                        <!-- <p class="font-semibold mb-4">Graphic designer</p> -->
                                        <p class="text-gray-500 mb-2">
                                            {{ products.about }}
                                        </p>
                                        <p class="text-gray-500 font-bold pb-5">
                                            ₹ {{ products.price }}
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <hr class="h-px my-2 bg-gray-200 border-0 dark:bg-gray-700">
                            <button
                                class="rounded-lg bg-green-500 text-white active:bg-green-500 uppercase text-sm px-6 py-3 shadow hover:bg-white hover:text-black hover:border-green-500 hover:border-2mr-1 mb-5 ease-linear transition-all duration-150"
                                type="button" @click="donate(products.item, products.price)"> donate now
                            </button>
                        </div>
                        <hr class="h-px my-2 bg-gray-200 border-0 dark:bg-gray-700">
                    </div>

                    <div style="font-size: 2rem;" class="mt-3 text-gray-600">Other Donation</div>
                    <p class="text-gray-500">Donate via</p>

                    <div class="flex">
                        <div class="">
                            <ul class="flex list-none flex-wrap flex-row text-center text-gray-500 text-xs">
                                <li class="flex">
                                    <div class="cursor-pointer rounded-t-lg">
                                        <img src="../../src/assets/Inter/img/phonepay.png" class="w-16 h-16">
                                        <p>Phone Pay</p>
                                    </div>
                                </li>
                                <li class="flex ml-5">
                                    <div class="cursor-pointer rounded-t-lg">
                                        <img src="../../src/assets/Inter/img/gpay.png" class="w-16 h-16">
                                        <p>Google Pay</p>
                                    </div>
                                </li>
                                <li class="flex ml-5">
                                    <div class="cursor-pointer rounded-t-lg">
                                        <img src="../../src/assets/Inter/img/bhim.png" class="w-16 h-16">
                                        <p>Bhim UPI</p>
                                    </div>
                                </li>
                                <li class="flex ml-5">
                                    <div class="cursor-pointer rounded-t-lg">
                                        <img src="../../src/assets/Inter/img/paytm.png" class="w-16 h-16">
                                        <p>Paytm</p>
                                    </div>
                                </li>
                                <li class="flex">
                                    <div class="cursor-pointer rounded-t-lg">
                                        <img src="../../src/assets/Inter/img/crditcard.png" class="w-16 h-16">
                                        <p>cr/dr card</p>
                                    </div>
                                </li>
                                <li class="flex ml-5">
                                    <div class="cursor-pointer rounded-t-lg">
                                        <img src="../../src/assets/Inter/img/banktransfer.png" class="w-16 h-16">
                                        <p>Bank Transfer</p>
                                    </div>
                                </li>
                                <li class="flex ml-5">
                                    <div class="cursor-pointer rounded-t-lg">
                                        <img src="../../src/assets/Inter/img/giftcard.png" class="w-16 h-16">
                                        <p>Gift Card</p>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>


                    <div style="font-size: 2rem;" class="mt-3">Donors</div>


                    <div class="flex flex-wrap">
                        <div class="w-full">
                            <ul class="flex mb-0 list-none flex-wrap pt-3 pb-4 flex-row">
                                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                                    <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal cursor-pointer"
                                        v-on:click="toggleTabs(1)"
                                        v-bind:class="{ 'bg-white': openTab !== 1, 'text-green-500': openTab === 1 }">
                                        <i class="fas fa-space-shuttle text-base mr-1"></i> Recent
                                    </a>
                                </li>
                                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                                    <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal cursor-pointer"
                                        v-on:click="toggleTabs(2)"
                                        v-bind:class="{ 'bg-white': openTab !== 2, 'text-green-500': openTab === 2 }">
                                        <i class="fas fa-cog text-base mr-1"></i> most generous
                                    </a>
                                </li>
                            </ul>
                            <div
                                class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded">
                                <div class="px-4 py-5 flex-auto">
                                    <div class="tab-content tab-space overflow-y-auto h-40">
                                        <div v-bind:class="{ 'hidden': openTab !== 1, 'block': openTab === 1 }">

                                            <!-- {{ recent_donation }} -->
                                            <div v-for="donation in recent_donation">

                                                <div class="flex items-center">
                                                    <img class="w-10 h-10 rounded-full" :src="donation.donor_image">
                                                    <div class="text-sm">
                                                        <p v-if="donation.anonymous != 1"
                                                            class="text-gray-900 leading-none font-bold">{{
                                                                donation.donor_name
                                                            }}</p>
                                                        <p v-else class="font-bold">Anonymous</p>
                                                        <p class="text-gray-600">{{ donation.creation }}</p>
                                                    </div>
                                                    <p class="pl-2">₹ {{ donation.amount }}</p>
                                                </div>

                                                <div class="block rounded-lg shadow-lg bg-white">
                                                    <!-- <div class="flex flex-wrap items-center">
                                            <div class="lg:flex lg:w-2/12 xl:w-3/12">
                                            <img :src="image" :alt="image"
                                                class="rounded-full"/>
                                            </div>
                                            <div class="lg:w-8/12 xl:w-9/12">
                                                <div>
                                                    <h4 v-if="donation.anonymous != 1" class="font-bold">{{ donation.donor_name }}</h4>
                                                    <h4 v-else class="font-bold">Anonymous</h4>
                                                    <p>{{ donation.creation }}</p>
                                                </div>
                                                <div>
                                                    {{ donation.amount }}
                                                </div>
                                            </div>
                                        </div> -->
                                                    <!-- <hr class="h-px my-2 bg-gray-200 border-0 dark:bg-gray-700"> -->
                                                </div>
                                                <hr class="h-px my-2 bg-gray-200 border-0 dark:bg-gray-700">
                                            </div>
                                        </div>
                                        <div v-bind:class="{ 'hidden': openTab !== 2, 'block': openTab === 2 }">
                                            <p>
                                                {{ tab2 }}
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <section class="bg-white dark:bg-gray-900">
                <div>
                    <section class="text-gray-700">
                        <div class="px-5 py-10">
                            <div class="mb-8">
                                <h1 class="text-7xl text-green-500 font-semibold text-center title-font mb-4 ">
                                    FAQ
                                </h1>
                                <p class="text-base leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto">
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet, voluptate!
                                </p>
                            </div>
                            <div class="flex flex-wrap sm:mx-auto sm:mb-2 mx-auto">
                                <div class="w-full py-2">
                                    <details class="mb-4">
                                        <summary
                                            class="font-semibold border-2 border-b-4 border-solid border-gray-200 text-xl text-green-500 list-none bg-gray-100 rounded py-2 px-4">
                                            What is Donatekart ?
                                        </summary>

                                        <span>
                                            <p
                                                class="border-2 border-solid border-gray-200 border-t-0 p-5 text-lg text-gray-500 dark:text-gray-300">
                                                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
                                                terry richardson ad squid. 3
                                                wolf moon officia aute, non cupidatat skateboard dolor brunch. Food
                                                truck quinoa nesciunt laborum
                                                eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid
                                                single-origin coffee nulla
                                                assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer
                                                labore wes anderson cred nesciunt
                                                sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings
                                                occaecat craft beer
                                                farm-to-table.
                                            </p>
                                        </span>
                                    </details>
                                    <details class="mb-4">
                                        <summary
                                            class="font-semibold border-2 border-b-4 border-solid border-gray-200 text-green-500 text-xl list-none bg-gray-100 rounded py-2 px-4">
                                            How to claim Tax-Exemption for my contributions on Donatekart?
                                        </summary>

                                        <span>
                                            <p
                                                class="border-2 border-solid border-gray-200 border-t-0 p-5 text-lg text-gray-500 dark:text-gray-300">
                                                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
                                                terry richardson ad squid. 3
                                                wolf moon officia aute, non cupidatat skateboard dolor brunch. Food
                                                truck quinoa nesciunt laborum
                                                eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid
                                                single-origin coffee nulla
                                                assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer
                                                labore wes anderson cred nesciunt
                                                sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings
                                                occaecat craft beer
                                                farm-to-table, raw denim aesthetic synth nesciunt you probably haven't
                                                heard of them accusamus labore
                                                sustainable VHS.</p>
                                        </span>
                                    </details>
                                    <details class="mb-4">
                                        <summary
                                            class="font-semibold border-2 border-b-4 border-solid border-gray-200 text-green-500 text-xl list-none bg-gray-100 rounded py-2 px-4">
                                            How to Donate ?
                                        </summary>

                                        <span>
                                            <p
                                                class="border-2 border-solid border-gray-200 border-t-0 p-5 text-lg text-gray-500 dark:text-gray-300">
                                                Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus
                                                terry richardson ad squid. 3
                                                wolf moon officia aute, non cupidatat skateboard dolor brunch. Food
                                                truck quinoa nesciunt laborum
                                                eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid
                                                single-origin coffee nulla
                                                assumenda shoreditch et.</p>
                                        </span>
                                    </details>
                                </div>

                            </div>
                        </div>
                    </section>
                </div>
            </section>
        </div>
    </div>
    <Footer />
</template>

<script>
import { ContentMatch } from 'prosemirror-model';
import { useRoute } from 'vue-router';
import { inject } from 'vue';
import axios from 'axios';
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
// import DonationDetail from "../components/DonationDetail.vue";
// import DonationDetailRightside from "../components/DonationDetailRightSide.vue";
export default {
    name: "CampaignDonation",
    components: {
        // DonationDetail,
        // DonationDetailRightside
        Navbar,
        Footer
    },
    setup() {
        const user = inject("user")
        return {
            user
        }
    },
    data() {
        return {
            campaign_detail: '',
            openTab: 1,
            recent_donation: '',
            campaign: '',
            tab2: 'this is tab two content',
            a: 70,
        }
    },
    mounted() {
        const name = useRoute();
        this.campaign = name.params.name
        this.get_campaign_donation_detail(name.params.name)
        this.get_recent_donation(name.params.name)
    },
    resources: {
        // get_campaign_donation_detail(){
        //     return{
        //         // method: '/api/method/sadbhavna_donatekart.api.campaign.get_campaign_detail',
        //         method: "api/resource/Donation Campaign/GIVE-TH-16-01-2023-0001",
        //         onSuccess: (res) => {
        //             console.log(res)
        //             this.campaign_detail = res
        //         },
        //         onError: (error) => {
        //             console.log(error)
        //         }
        //     }
        // }

        get_recent_donation() {
            return {
                method: "sadbhavna_donatekart.api.api.get_recent_donation",
                onSuccess: (res) => {
                    this.recent_donation = res
                },
                onError: (error) => {
                    console.log(error)
                }
            }
        },
        set_details_in_doctype_after_donation() {
            return {
                method: "sadbhavna_donatekart.api.api.set_details_in_doctype_after_donation",
                onSuccess: (res) => {
                    alert("your donation is successfull")
                },
                onError: (error) => {
                    alert("Something Want Wrong!", error)
                }
            }
        }

    },
    methods: {
        toggleTabs: function (tabNumber) {
            this.openTab = tabNumber
        },
        get_campaign_donation_detail(name) {
            let url = "/api/resource/Donation Campaign/" + name
            fetch(url, {
                method: 'GET',
            })
                .then(response => {
                    response.json().then(res => {
                        this.campaign_detail = res
                    });
                })
                .catch(err => {
                    console.error(err);
                });
        },
        get_recent_donation(name) {
            // let url = `/api/resource/Donation?filters={[['campaign': ${name}], ['anonymous': 0]]}`
            // axios.get(url).then((response) => {
            //   this.recent_donation = response.data['data']
            // }).catch(function (error){
            //   console.log(error);
            // })
            this.$resources.get_recent_donation.submit({
                name: name
            })

        },
        donate(name, price) {
            if (!this.user.isLoggedIn()) {
                console.log("if not logged in")
                this.$router.push(`/sadbhavna/login`)
                // return
            }
            else {
                console.log("if login")
                const cookie = Object.fromEntries(
                document.cookie
                    .split("; ")
                    .map((part) => part.split("="))
                    .map((d) => [d[0], decodeURIComponent(d[1])])
            )
            this.$resources.set_details_in_doctype_after_donation.submit({
                user_id: cookie.user_id,
                campaign: this.campaign,
                item: name,
                price: price
            })
                // this.$router.push(`/sadbhavna/donate/${name}&${price}`)
            }
        },

        // get_campaign_donation_detail(name){
        //     // axios.get('/api/resource/Donation Campaign/GIVE-TH-16-01-2023-0001').then((response) => {
        //     //     console.log(response.data)
        //     // })

        //     this.$resources.get_campaign_donation_detail.submit({
        // 		name: name
        // 	})

        // }

        set_details_in_doctype_after_donation(name, price) {
            const cookie = Object.fromEntries(
                document.cookie
                    .split("; ")
                    .map((part) => part.split("="))
                    .map((d) => [d[0], decodeURIComponent(d[1])])
            )
            this.$resources.set_details_in_doctype_after_donation.submit({
                user_id: cookie.user_id,
                campaign: this.campaign,
                item: name,
                price: price
            })
        }

    }
}
</script>