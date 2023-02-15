<template>
  <div class="pt-2 pl-2 md:pl-10 lg:pl-28 pr-2 md:pr-10 lg:pr-28">
    <nav class="rounded-xl flex items-center flex-wrap p-6 justify-between bg-green-500">

      <div class="flex items-center flex-shrink-0 text-white mr-6 ">
        <img src="../../src/assets/Inter/img/logo.png" class="w-48 h-20 ml-6" />
      </div>
      <div class="block lg:hidden">
        <button @click="isOpen = !isOpen"
          class="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white">
          <svg v-if="isOpen" class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <title>Menu</title>
            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
          </svg>
          <svg v-if="!isOpen" class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <title>Menu</title>
            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
          </svg>
        </button>
      </div>

      <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto ">
        <div :class="isOpen ? 'block' : 'hidden'" class="text-sm lg:flex-grow">
          <a href="/home" class="block mt-4 font-bold lg:inline-block lg:mt-0 text-white hover:text-black mr-4 ">
            Home
          </a>
          <a href="#" class="block mt-4 font-bold lg:inline-block lg:mt-0 text-white hover:text-black mr-4">
            About
          </a>
          <div class="block mt-4 lg:inline-block font-bold lg:mt-0 text-white hover:text-black mr-4 cursor-pointer" @click="this.$router.push(`/sadbhavna/request-campaign`)">
            Request a Campaign
          </div>
          <a href="/sadbhavna/contact-us" class="block font-bold mt-4 lg:inline-block lg:mt-0 text-white hover:text-black mr-4">
            Contact Us
          </a>
          <span class="group relative inline-block">
            <a href="#" class="block mt-4 lg:inline-block font-bold lg:mt-0 text-white hover:text-black mr-4">
              Blog
            </a>
            <ul class="absolute hidden pt-1 text-gray-700 group-hover:block">
              <li class=""><a class="whitespace-pre block bg-white py-2 px-4" href="#">Blog</a></li>
              <li class=""><a class="whitespace-pre block bg-white py-2 px-4" href="#">Single - Blog</a></li>
            </ul>
          </span>
          <span class="group relative inline-block">
            <a href="#" class="block mt-4 lg:inline-block font-bold lg:mt-0 text-white hover:text-black mr-4">
              Page
            </a>
            <ul class="absolute hidden pt-1 text-gray-700 group-hover:block">
              <li class=""><a class="whitespace-pre block bg-white py-2 px-4" href="#">Elements</a></li>
              <li class=""><a class="whitespace-pre block bg-white py-2 px-4" href="#">Cause</a></li>
            </ul>
          </span>
          <div v-if="this.user.isLoggedIn()" @click="profile()"
            class="block mt-4 lg:inline-block lg:mt-0 text-white cursor-pointer hover:text-black  mr-4">
            profile
        </div>

        </div>
        <div>
          <button v-if="this.user.isLoggedIn()" @click="logout()"
            class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0">Logout</button>
          <button v-else @click="this.$router.push(`/sadbhavna/login`)"
            class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0">Login</button>
        </div>
      </div>
    </nav>
  </div>


</template>

<script>
import axios from "axios";
import { inject } from "vue";
export default {
  name: "Navbar",
  setup() {
    const user = inject("user")
    return {
      user
    }
  },
  data() {
    return {
      isOpen: true
    }
  },
  // resources: {
  //   logout(){
  //     console.log("logout 1")
  //     return{
  //       method: '/api/method/logout',
  //       onSuccess: () => {
  //         console.log("success")
  //       },
  //       onError: () => {
  //         console.log("error")
  //       }
  //     }
  //   }
  // },
  methods: {
    logout() {
      console.log("click logout")
      axios.get('/api/method/logout').then((res) => {
        this.$router.go()
      }).catch(function (error) {
        console.log("not okey")
      })
      // this.$resources.logout
    },

    profile() {
      const cookie = Object.fromEntries(
					document.cookie
						.split("; ")
						.map((part) => part.split("="))
						.map((d) => [d[0], decodeURIComponent(d[1])])
				)

				// return cookie.user_id
      this.$router.push(`/sadbhavna/profile/${cookie.user_id}`)
    }

  },

  mounted() {
    if (!this.user.isLoggedIn()) {
      // this.$router.push({
      // 	name: "DeskLogin",
      // 	query: { route: this.$route.path },
      // })
      return
    }
    // else{
    //   this.$router.push(`/sadbhavna/login`) 
    // }
    // if (!this.user.has_desk_access) {
    // 	this.$router.push({ path: "/home" })
    // 	return
    // }
  }
}
</script>