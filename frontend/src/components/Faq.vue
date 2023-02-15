<template>
    
    <div class="w-full h-[30rem] md:h-[32rem] lg:h-[36rem] bg-center bg-right bg-transparent bg-cover"
        style="background-image: url('../../src/assets/Inter/img/faq-bnr.jpg')">
        <Navbar />

        <div
            class="text-[30px] md:text-[36px] lg:text-[48px] container p-[160px] md:p-[192px] lg:p-[208px] text-center  text-green-500 font-bold mx-auto h-full">
            FAQ</div>

    </div>


    <div class="container mx-auto h-full pt-0">
        <div class="w-full bg-grey-lightest">
            <div class="container py-0">
                <div class="w-6/6 lg:w:4/6 mx-auto bg-white">
                    <div class="sm:pt-10">
                        <div class="mx-3 md:mx-4 lg:mx-5 border-solid border-b-2">
                            <ul class="flex justify-center mb-0 mt-10 flex-wrap pt-4 ml-10 mr-11  flex-row">
                                <li class="-mb-px mr-2 hover:shadow last:mr-0  text-center">
                                    <a class="text-[16px] md:text-[22px] lg:text-[22px] font-bold  px-5 md:px-3 lg:px-5 py-3 rounded block leading-normal"
                                        v-on:click="toggleTabs(1)"
                                        v-bind:class="{'text-green-500 bg-white': openTab !== 1, 'text-white bg-green-500': openTab === 1}">
                                        Recent
                                    </a>
                                </li>
                                <li class="-mb-px mr-2 hover:shadow last:mr-0  text-center">
                                    <a class="text-[16px] md:text-[22px] lg:text-[22px] font-bold  px-5 py-3 rounded block leading-normal"
                                        v-on:click="toggleTabs(2)"
                                        v-bind:class="{ 'text-green-500 bg-white': openTab !== 2, 'text-white bg-green-500': openTab === 2 }">
                                        Most Generous
                                    </a>
                                </li>
                            </ul>
                        </div>
                        <div class="px-0 py-px flex-auto">
                            <div class="tab-content tab-space">
                                <div v-bind:class="{ 'hidden': openTab !== 1, 'block': openTab === 1 }">
                                    <section class="text-gray-700">
                                        <div class="container px-0 py-7 mx-auto">

                                            <div class="">
                                                <div class="w-full lg:w-1/2 px-4 py-2">
                                                    <details class="mb-4">
                                                        <summary
                                                            class="font-semibold border-2 border-b-4 border-solid border-gray-200 text-xl text-green-500 list-none bg-gray-100 rounded py-3 px-4">
                                                            Collapsible Group Item #1
                                                        </summary>

                                                        <span>
                                                            <p
                                                                class="border-2 border-solid border-gray-200 border-t-0 p-5 text-lg text-gray-500 dark:text-gray-300">
                                                                Anim pariatur cliche reprehenderit, enim eiusmod high
                                                                life accusamus terry richardson ad squid. 3
                                                                wolf moon officia aute, non cupidatat skateboard dolor
                                                                brunch. Food truck quinoa nesciunt laborum
                                                                eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a
                                                                bird on it squid single-origin coffee nulla
                                                                assumenda shoreditch et. Nihil anim keffiyeh helvetica,
                                                                craft beer labore wes anderson cred
                                                                nesciunt sapiente ea proident. Ad vegan excepteur
                                                                butcher vice lomo. Leggings occaecat craft beer
                                                                farm-to-table, raw denim aesthetic synth nesciunt you
                                                                probably haven't heard of them accusamus
                                                                labore sustainable VHS.
                                                            </p>
                                                        </span>
                                                    </details>
                                                    <details class="mb-4">
                                                        <summary
                                                            class="font-semibold border-2 border-b-4 border-solid border-gray-200 text-green-500 text-xl list-none bg-gray-100 rounded py-3 px-4">
                                                            Collapsible Group Item #2
                                                        </summary>

                                                        <span>
                                                            <p
                                                                class="border-2 border-solid border-gray-200 border-t-0 p-5 text-lg text-gray-500 dark:text-gray-300">
                                                                Anim pariatur cliche reprehenderit, enim eiusmod high
                                                                life accusamus terry richardson ad squid. 3
                                                                wolf moon officia aute, non cupidatat skateboard dolor
                                                                brunch. Food truck quinoa nesciunt laborum
                                                                eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a
                                                                bird on it squid single-origin coffee nulla
                                                                assumenda shoreditch et. Nihil anim keffiyeh helvetica,
                                                                craft beer labore wes anderson cred
                                                                nesciunt sapiente ea proident. Ad vegan excepteur
                                                                butcher vice lomo. Leggings occaecat craft beer
                                                                farm-to-table, raw denim aesthetic synth nesciunt you
                                                                probably haven't heard of them accusamus
                                                                labore sustainable VHS.</p>
                                                        </span>
                                                    </details>
                                                    <details class="mb-4">
                                                        <summary
                                                            class="font-semibold border-2 border-b-4 border-solid border-gray-200 text-green-500 text-xl list-none bg-gray-100 rounded py-3 px-4">
                                                            Collapsible Group Item #3
                                                        </summary>

                                                        <span>
                                                            <p
                                                                class="border-2 border-solid border-gray-200 border-t-0 p-5 text-lg text-gray-500 dark:text-gray-300">
                                                                Anim pariatur cliche reprehenderit, enim eiusmod high
                                                                life accusamus terry richardson ad squid. 3
                                                                wolf moon officia aute, non cupidatat skateboard dolor
                                                                brunch. Food truck quinoa nesciunt laborum
                                                                eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a
                                                                bird on it squid single-origin coffee nulla
                                                                assumenda shoreditch et. Nihil anim keffiyeh helvetica,
                                                                craft beer labore wes anderson cred
                                                                nesciunt sapiente ea proident. Ad vegan excepteur
                                                                butcher vice lomo. Leggings occaecat craft beer
                                                                farm-to-table, raw denim aesthetic synth nesciunt you
                                                                probably haven't heard of them accusamus
                                                                labore sustainable VHS.</p>
                                                        </span>
                                                    </details>
                                                </div>

                                            </div>
                                        </div>
                                    </section>
                                </div>
                                <div v-bind:class="{ 'hidden': openTab !== 2, 'block': openTab === 2 }">
                                    <div class="container text-gray-600 py-7 px-3 md:px-4 lg:px-0 mx-auto">
                                        profile
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
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
export default {
    name: "requester_type",
    components: {
        Navbar,
        Footer
    },
    data() {
        return {
            openTab: 1
        }
    },
    methods: {
        toggleTabs: function (tabNumber) {
            this.openTab = tabNumber
        }
    }
}
</script>