<!-- <style>
.img{
  height: 200px;
  width: 200px;
}
</style> -->

<template> 
<!-- <div class="flex flex-wrap"> -->
  <div v-for="data in campaigns"> 
    <div class="card" style="width: 18rem;">
      <img class="card-img-top" v-bind:src="data.campain_image" alt="asdf" @click="viewmore(data.name)">
      <div class="card-body" @click="viewmore(data.name)">
        <h5 class="card-title">{{data.campaign_category}}</h5>
        <p class="card-text">by: {{data.ngo}}</p>
        <p class="card-text">{{data.raised_amount}} raised out of {{data.donation_amount}}</p>
         <div class="progress">
          <div class="progress-bar bg-warning" style="width:{{data.raised_amount*100/data.donation_amount}}%"></div>
         </div><br>        
      </div>
      <!-- <Button @click="viewmore(data.name)" appearance="primary">View More</Button> -->
      <button href="#">share</button>
      <button class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" @click="donate(data.name)"> donate now </button>
        <!-- <Button @click="donate(data.name)" appearance="danger">Donate</Button> -->
    </div>
  </div>
<!-- </div> -->


<!-- ///////////////// -->

<!-- <div class="flex flex-wrap">
  <div v-for="data in campaigns"> 
    <div class="w-full px-4" style="width: 18rem;">
      <img class="card-img-top" v-bind:src="data.campain_image" alt="asdf" @click="viewmore(data.name)">
      <Button @click="viewmore(data.name)" appearance="primary">View More</Button>
      <button href="#">share</button>
      <button class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" @click="donate(data.name)"> donate now </button>
        <Button @click="donate(data.name)" appearance="danger">Donate</Button>
    </div>
  </div>
</div> -->

<!-- <div>
  <b-card-group deck>
    <b-card
      header="featured"
      header-tag="header"
      footer="Card Footer"
      footer-tag="footer"
      title="Title"
    >
      <b-card-text>Header and footers using props.</b-card-text>
      <b-button href="#" variant="primary">Go somewhere</b-button>
    </b-card>

    <b-card title="Title" header-tag="header" footer-tag="footer">
      <template #header>
        <h6 class="mb-0">Header Slot</h6>
      </template>
      <b-card-text>Header and footers using slots.</b-card-text>
      <b-button href="#" variant="primary">Go somewhere</b-button>
      <template #footer>
        <em>Footer Slot</em>
      </template>
    </b-card>
  </b-card-group>
</div> -->

 <!-- <div class="max-w-3xl py-12 mx-auto">
  <router-link to="/sadbhavna/login">Login</router-link>
  <div class="row">
    <div v-for="data in campaigns">
      <div class="col">
        <img v-bind:src="data.campain_image" class="img" />
        <h3>{{ data.campaign_title }}</h3>
        <div> {{ data.donation_amount - data.raised_amount }} </div>
      </div>
    </div>
  </div>
</div> -->

 <!-- <div class="row">
    <div class="col-md-4" v-for="data in campaigns">
          <div class="card h-100">
            <img class="card-img-top" v-bind:src="data.campaign_image" alt="card image collar">
            <div class="card-body">
              <h5 class="card-title">Product</h5>
              <p class="card-text">asdf adsf asdfasdf</p>
              <button v-on:click="addProductToCart(product)" class="btn btn-primary">Add To Cart</button>
            </div>
          </div>
     </div>
 </div> -->

</template>


<!-- <template>
  <vue-card-stack :cards="cards">
  <template v-slot:card="{ card }">
    <div
      :style="{ background: card.background }"
      style="width: 100%; height: 100%;"
    ></div>
  </template>
</vue-card-stack>
</template> -->

<!-- 
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
    >
      <v-card-title>Top 10 Australian beaches</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>Whitehaven Beach</div>

      <div>Whitsunday Island, Whitsunday Islands</div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
      >
        Share
      </v-btn>

      <v-btn
        color="orange"
        text
      >
        Explore
      </v-btn>
    </v-card-actions>
  </v-card>
</template> -->


<!-- <template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-img
      class="white--text align-end"
      height="200px"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
    >
      <v-card-title>Top 10 Australian beaches</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">Number 10</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>Whitehaven Beach</div>

      <div>Whitsunday Island, Whitsunday Islands</div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
      >
        Share
      </v-btn>

      <v-btn
        color="orange"
        text
      >
        Explore
      </v-btn>
    </v-card-actions>
  </v-card> -->

<!-- <v-container class="my-5">
  <v-layout row wrap>
    <v-flex xs12 sm6 md4 lg3 v-for="data in campaigns" :key="data.name">
      <v-card flat class="text-xs-center ma-3">{{ data.campaign_title }}</v-card>
    </v-flex>
  </v-layout>
</v-container> -->

<!-- <v-card class="row" height="550" style="overflow-y: scroll; overflow-x: hidden">
    Your card body           
</v-card>
<v-card class="row" height="450" style="overflow-y: scroll; overflow-x: hidden">
    Your card body           
</v-card> -->
<!-- </template> -->




<!-- <template>
  <Disclosure as="nav" class="bg-gray-800" v-slot="{ open }">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
        
          <DisclosureButton class="inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
            <span class="sr-only">Open main menu</span>
            <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
        <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
          <div class="flex flex-shrink-0 items-center">
            <img class="block h-8 w-auto lg:hidden" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company" />
            <img class="hidden h-8 w-auto lg:block" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company" />
          </div>
          <div class="hidden sm:ml-6 sm:block">
            <div class="flex space-x-4">
              <a v-for="item in navigation" :key="item.name" :href="item.href" :class="[item.current ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white', 'px-3 py-2 rounded-md text-sm font-medium']" :aria-current="item.current ? 'page' : undefined">{{ item.name }}</a>
            </div>
          </div>
        </div>
        <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
          <button type="button" class="rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
            <span class="sr-only">View notifications</span>
            <BellIcon class="h-6 w-6" aria-hidden="true" />
          </button>

        
          <Menu as="div" class="relative ml-3">
            <div>
              <MenuButton class="flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                <span class="sr-only">Open user menu</span>
                <img class="h-8 w-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
              </MenuButton>
            </div>
            <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
              <MenuItems class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <MenuItem v-slot="{ active }">
                  <a href="#" :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']">Your Profile</a>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <a href="#" :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']">Settings</a>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <a href="#" :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']">Sign out</a>
                </MenuItem>
              </MenuItems>
            </transition>
          </Menu>
        </div>
      </div>
    </div>

    <DisclosurePanel class="sm:hidden">
      <div class="space-y-1 px-2 pt-2 pb-3">
        <DisclosureButton v-for="item in navigation" :key="item.name" as="a" :href="item.href" :class="[item.current ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white', 'block px-3 py-2 rounded-md text-base font-medium']" :aria-current="item.current ? 'page' : undefined">{{ item.name }}</DisclosureButton>
      </div>
    </DisclosurePanel>
  </Disclosure>
</template> -->
<!-- 
<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { Bars3Icon, BellIcon, XMarkIcon } from '@heroicons/vue/24/outline'

const navigation = [
  { name: 'Dashboard', href: '#', current: true },
  { name: 'Team', href: '#', current: false },
  { name: 'Projects', href: '#', current: false },
  { name: 'Calendar', href: '#', current: false },
]
</script> -->





<script>
import axios from 'axios';


export default {
  name: 'Home',
  created(){
    this.get_campaigns()
    },
  data() {
    return {
      campaigns: [],
      loading: false,
      selection: 1,
      // cards: [
      //   { background: "#00659d" },
      //   { background: "#00abbc" },
      //   { background: "#e2c58a" },
      //   { background: "#fc8890" },
      //   { background: "#b35d7f" },
      // ],
    }
  },
  resources: {
    
  },
  methods:{
    get_campaigns(){
      axios.get('/api/resource/Donation Campaign?filters={"published": 1}&fields=["name", "campain_image", "campaign_title", "donation_amount", "raised_amount", "start_date", "end_date", "short_description", "ngo", "campaign_category"]').then((response) => {
          this.campaigns = response.data['data']
        }).catch(function (error){
          console.log(error);
        })
    },
    reserve () {
        this.loading = true
        setTimeout(() => (this.loading = false), 2000)
      },
    viewmore(name){
      this.$router.push(`/sadbhavna/campaign-donation/${name}`)
    },
    donate(name){
      this.$router.push(`/sadbhavna/donate/${name}`)
    }

},
  components: {

  },
  // mounted: {
  //   data
  // }

  // beforeMount(){
  //   this.get_campaign
  // }
}

</script>
