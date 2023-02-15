<template>
    <Navbar />
    <div class="container mx-auto h-full">
        
        <div class="w-full sm:pt-0 md:pt-5 lg:pt-12 bg-grey-lightest">
            <div class="container mx-auto py-0">
                <div class="w-6/6 lg:w:4/6 mx-auto bg-white">
                    <div class="py-8 px-10 text-gray-600 text-black text-center text-4xl">Donation Campaign request
                    </div>
                    <div class="flex flex-wrap">
                        <div class=" sm:p-10 ">
                            <ul class="flex  mb-0 flex-wrap pt-4 ml-10 mr-11 pb-4 flex-row">
                                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                                    <a class="text-base font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
                                        v-on:click="toggleTabs(1)"
                                        v-bind:class="{'text-green-500 bg-white': openTab !== 1, 'text-white bg-green-500': openTab === 1}">
                                        NGO
                                    </a>
                                </li>
                                <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
                                    <a class="text-base font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
                                        v-on:click="toggleTabs(2)"
                                        v-bind:class="{ 'text-green-500 bg-white': openTab !== 2, 'text-white bg-green-500': openTab === 2 }">
                                        Individual Group
                                    </a>
                                </li>
                            </ul>
                            <div class="px-4 py-5 flex-auto">
                                <div class="tab-content tab-space">
                                    <div class="py-4 px-8">
                                        <div class="mb-4">
                                            <label class="block text-gray-600 text-base  mb-2" for="email">Full
                                                Name</label>
                                            <input
                                                class="appearance-none border-gray-300  hover:border-green-500 rounded w-full py-2 px-3 text-grey-darker"
                                                v-model="full_name" type="text" required>
                                        </div>
                                        <div v-if="openTab == 1"
                                            class="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-4">
                                            <div class="mb-4">
                                                <label class="block text-gray-600 text-base  mb-2">Organisation
                                                    Name</label>
                                                <input
                                                    class="appearance-none border-gray-300 rounded w-full py-2 px-3 hover:border-green-500 text-grey-darker"
                                                    type="text" v-model="organisation_name" required>
                                            </div>
                                            <div class="mb-4">
                                                <label class="block text-gray-600 text-base  mb-2">Organisation
                                                    Website</label>
                                                <input
                                                    class="appearance-none border-gray-300 hover:border-green-500 rounded w-full py-2 px-3 text-grey-darker"
                                                    type="text" v-model="organisation_website" required>
                                            </div>
                                        </div>
                                        <div class="grid sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-3 gap-4">
                                            <div class="mb-6">
                                                <label class="block text-gray-600 text-base  mb-2">Phone</label>
                                                <input
                                                    class="appearance-none border-gray-300 hover:border-green-500 rounded w-full py-2 px-3 text-grey-darker"
                                                    type="text" v-model="phone" required>
                                            </div>
                                            <div class="mb-6">
                                                <label class="block text-gray-600 text-base  mb-2">Email</label>
                                                <input
                                                    class="appearance-none border-gray-300 hover:border-green-500 rounded w-full py-2 px-3 text-grey-darker"
                                                    type="email" v-model="email" required>
                                            </div>
                                            <div class="mb-6">
                                                <label class="block text-gray-600 text-base  mb-2">Social Media
                                                    Page</label>
                                                <input
                                                    class="appearance-none border-gray-300 hover:border-green-500 rounded w-full py-2 px-3 text-grey-darker"
                                                    type="text" v-model="social_media_page" required>
                                            </div>
                                        </div>
                                        <div class="grid sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-2 gap-4">
                                            <div class="mb-6">
                                                <label class="block text-gray-600 text-base  mb-2">Campaign
                                                    Story</label>
                                                <textarea id="comment" rows="4" v-model="campaign_story"
                                                    class="hover:border-green-500 w-full px-0 text-sm text-gray-900 bg-white border-1 border-gray-300  focus:ring-0 dark:text-white dark:placeholder-gray-600"
                                                    required></textarea>
                                            </div>
                                            <div class="mb-6">
                                                <label class="block text-gray-600 text-base  mb-2">Beneficiary
                                                    Group</label>
                                                <textarea id="comment" rows="4" v-model="beneficiary_group"
                                                    class="hover:border-green-500 w-full px-0 text-sm text-gray-600 bg-white border-1 border-gray-300  focus:ring-0 dark:text-white dark:placeholder-gray-600"
                                                    required></textarea>
                                            </div>
                                        </div>
                                        <div class="mb-6">
                                            <button
                                                class="appearance-none border-gray-600 rounded w-full py-2 px-3 text-grey-darker bg-green-500 hover:bg-transparent text-white hover:text-green-500 py-2 tracking-wide px-4 border border-green-500 hover:border-green-500  text-lg uppercase rounded" @click="request_campaign()">Submit</button>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <Footer />
</template>
   
<script>
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";

export default {
    name: "Donation Campaign Request",
    components: {
    Navbar,
    Footer
  },
    data() {
        return {
            openTab: 1,
            full_name: '',
            campaign_type: '',
            organisation_name: '',
            organisation_website: '',
            email: '',
            phone: '',
            campaign_story: '',
            social_media_page: '',
            beneficiary_group: ''
        }
    },
    resources: {
        request_campaign() {
            return {
                method: 'sadbhavna_donatekart.api.campaign.request_campaign',
                onSuccess: (res) => {
                    // this.recent_donation = res
                   alert("Your Request is successfully sent to sadbhavna donatekart")
                },
                onError: (error) => {
                    console.log(error)
                    alert("Something Want Wrong!", error)
                }
            }
        }
    },

    methods: {
        toggleTabs: function (tabNumber) {
            this.openTab = tabNumber
            this.tab = this.tabNumber
        },
        request_campaign() {
            // console.log("opentab", this.openTab)
            if (this.openTab == 1) {
                this.campaign_type = 'NGO'
            }
            else {
                this.campaign_type = 'Indivisual/Group'
            }
            this.$resources.request_campaign.submit({
                full_name: this.full_name,
                campaign_type: this.campaign_type,
                organisation_name: this.organisation_name,
                organisation_website: this.organisation_website,
                email: this.email,
                phone: this.phone,
                campaign_story: this.campaign_story,
                social_media_page: this.social_media_page,
                beneficiary_group: this.beneficiary_group
            })

        }
    }
}
</script>