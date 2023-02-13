<template>

  <Navbar />


  <div class="relative overflow-hidden bg-no-repeat bg-cover"
    style="background-image: url('../../src/assets/Inter/img/Frame1.jpg')">
    <div class="container mx-auto h-full">
      <div class="grid lg:grid-cols-2 m-10">

        <div class="lg:pt-64 sm:pt-8 pr-10">
          <p class="text-green-500 font-sans text-3xl font-bold">
            Donate with on
            <span class="text-gray-700">100% Transparency</span>
            on
            <span class="text-gray-700">most trusted</span>
            crowd funding platform of India.
          </p>
        </div>
        <div class="lg:p-0 sm:p-14">
          <img src="../../src/assets/Inter/img/map2.png" class="" />
        </div>
      </div>
    </div>
  </div>




  <!-- <div class="bg-auto w-full h-full bg-local bg-center bg-cover" style="background-image: url('../../src/assets/Inter/img/Frame1.jpg')"> 
 
 <div class="sm:justify-items-center md:justify-items-center lg:justify-items-start  grid lg:grid-cols-2 pt-0 md:pt-10 lg:pt-32 ">
 
       <div class="lg:text-left sm:text-center md:text-center">
        <p class="pt-64 lg:pl-64 md:pl-0 sm:pl-16 lg:pr-0 sm:pr-16 drop-shadow-2xl text-green-500 font-sans text-3xl font-bold hover:font-sans">
        Donate with on       
        <span class="drop-shadow-2xl text-gray-700">100% Transparency</span>
        on
        <span class="drop-shadow-2xl text-gray-700">most trusted</span>
        crowd funding platform of India.</p>
       </div>
       <div class="mt-20 h-auto max-w-sm">
         <img src="../../src/assets/Inter/img/map2.png" class=""/>
       </div>
 
 </div>
 </div> -->


  <div class="container mx-auto h-full">


    <!-- <div class="flex flex-wrap bg-white shadow-lg mt-5">
      <div class="w-full lg:w-6/12 md:w-6/12 justify-self-center mt-40">
        <p class="drop-shadow-2xl text-green-500 font-sans text-3xl font-bold hover:font-sans">
          Donate with on
          <span class="drop-shadow-2xl text-gray-700">100% Transparency</span>
          on
          <span class="drop-shadow-2xl text-gray-700">most trusted</span>
          crowd funding platform of India.
        </p>
      </div>
      <div class="w-full lg:w-6/12 md:w-6/12">
        <img class="sm:mb-3" src="../../src/assets/Inter/img/map2.png" alt="" />
      </div>
    </div> -->





    <div class="flex flex-wrap bg-white shadow-lg mt-5">
      <div class="w-full lg:w-4/12 md:w-4/12">
        <img class="sm:mb-3" src="../../src/assets/Inter/img/Old-Lady.png" alt="" />
      </div>
      <div class="w-full lg:w-8/12 md:w-8/12">
        <div class="pl-6 justify-start">
          <button class="bg-gray-700 w-32 rounded-lg p-2 text-white mb-5 md:mt-3">Featured</button>
          <h5 class="text-gray-900 text-xl font-medium mb-2">This Australian Has Made India His Home To Feed Hundreds Of
            Poor People, Help Him</h5>
          <p class="text-gray-700 text-base mb-10">
            In a world that has seen a lot of pain and suffering, Th3 Lot wishes to bring back the smiles on helpless
            faces. You can join their mission.
          </p>
          <p class="text-green-500 mb-5 font-bold">Donate Now</p>
        </div>
      </div>
    </div>

    <!-- <div class="grid lg:grid-cols-1 md:grid-cols-1 sm:grid-cols-1 gap-2">
    <div v-for="data in campaigns">
    <div class="flex pt-10">  
      <div class="flex flex-col md:flex-row bg-white shadow-lg">
        <img class="w-5/12" src="../../src/assets/Inter/img/Old-Lady.png" alt="" />
        <div class="pl-6 flex flex-col justify-start">
          <button class="bg-gray-700 w-20 rounded-lg text-sm p-2 text-white mb-5">Featured</button>
          <h5 class="text-gray-900 text-xl font-medium mb-2">This Australian Has Made India His Home To Feed Hundreds Of
            Poor People, Help Him</h5>
          <p class="text-gray-700 text-base mb-10">
            In a world that has seen a lot of pain and suffering, Th3 Lot wishes to bring back the smiles on helpless
            faces. You can join their mission.
          </p>
          <p class="text-green-500 mb-5 font-bold">Donate Now</p>
        </div>
      </div>
    </div>
    </div>
    </div> -->

    <div class="text-center mt-10">
      <h2 class="text-4xl font-bold text-green-500 mb-2">Categories</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet, voluptate!</p>
    </div>



    <div class="flex mt-3">
      <div class="overflow-x-auto">
        <ul class="flex mb-0 list-none pt-3 pb-4">
          <li class="-mb-px mr-2 last:mr-0 text-center" @click="get_campaigns()">
            <div class="font-bold px-5 py-3 cursor-pointer hover:bg-green-500 rounded-t-lg h-30 w-30"
              v-on:click="toggleTabs(1)"
              v-bind:class="{ 'bg-gray-300': openTab !== 1, 'rounded-t-lg bg-green-500': openTab === 1 }">
              <!-- <div class="text-gray-700 text-center bg-green-500 px-4 py-2 m-2"> -->
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/grid.png" />All
              <!-- </div> -->
            </div>
          </li>
          <li class="-mb-px mr-2 last:mr-0 text-center" @click="get_campaigns('Animal Campaign')">
            <div class="font-bold px-5 py-3 cursor-pointer hover:bg-green-500 rounded-t-lg h-30 w-30"
              v-on:click="toggleTabs(2)"
              v-bind:class="{ 'bg-gray-300': openTab !== 2, 'rounded-t-lg bg-green-500': openTab === 2 }">
              <!-- <div class="text-gray-700 text-center px-4 py-2 m-2"> -->
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/paw.png" />Animal
              <!-- </div> -->
            </div>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center" @click="get_campaigns('Education Campaign')">
            <div class="font-bold px-5 py-3 cursor-pointer hover:bg-green-500 rounded-t-lg h-30 w-30"
              v-on:click="toggleTabs(3)"
              v-bind:class="{ 'bg-gray-300': openTab !== 3, 'rounded-t-lg bg-green-500': openTab === 3 }">
              <!-- <div class="text-gray-700 text-center bg-green-500 px-4 py-2 m-2"> -->
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/edu.png" />Education
              <!-- </div> -->
            </div>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center" @click="get_campaigns('Children Campaign')">
            <div class="font-bold px-5 py-3 cursor-pointer hover:bg-green-500 rounded-t-lg h-30 w-30"
              v-on:click="toggleTabs(4)"
              v-bind:class="{ 'bg-gray-300': openTab !== 4, 'rounded-t-lg bg-green-500': openTab === 4 }">
              <!-- <div class="text-gray-700 text-center bg-green-500 px-4 py-2 m-2"> -->
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/children.png" />Children
              <!-- </div> -->
            </div>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center" @click="get_campaigns('Medical Campaign')">
            <div class="font-bold px-5 py-3 cursor-pointer hover:bg-green-500 rounded-t-lg h-30 w-30"
              v-on:click="toggleTabs(5)"
              v-bind:class="{ 'bg-gray-300': openTab !== 5, 'rounded-t-lg bg-green-500': openTab === 5 }">
              <!-- <div class="text-gray-700 text-center bg-green-500 px-4 py-2 m-2"> -->
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/healthcare.png " />Medical
              <!-- </div> -->
            </div>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center" @click="get_campaigns('Hunger Campaign')">
            <div class="font-bold px-5 py-3 cursor-pointer hover:bg-green-500 rounded-t-lg h-30 w-30"
              v-on:click="toggleTabs(6)"
              v-bind:class="{ 'bg-gray-300': openTab !== 6, 'rounded-t-lg bg-green-500': openTab === 6 }">
              <!-- <div class="text-gray-700 text-center bg-green-500 px-4 py-2 m-2"> -->
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/food.png" />Hunger
              <!-- </div> -->
            </div>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center" @click="get_campaigns('Religiouse Campaign')">
            <div class="font-bold px-5 py-3 cursor-pointer hover:bg-green-500 rounded-t-lg h-30 w-30"
              v-on:click="toggleTabs(7)"
              v-bind:class="{ 'bg-gray-300': openTab !== 7, 'rounded-t-lg bg-green-500': openTab === 7 }">
              <!-- <div class="text-gray-700 text-center bg-green-500 px-4 py-2 m-2"> -->
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/pray.png" />Religiouse
              <!-- </div> -->
            </div>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center" @click="get_campaigns('Disability Campaign')">
            <div class="font-bold px-5 py-3 cursor-pointer hover:bg-green-500 rounded-t-lg h-30 w-30"
              v-on:click="toggleTabs(8)"
              v-bind:class="{ 'bg-gray-300': openTab !== 8, 'rounded-t-lg bg-green-500': openTab === 8 }">
              <!-- <div class="text-gray-700 text-center bg-green-500 px-4 py-2 m-2"> -->
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/disability.png" />Disability
              <!-- </div> -->
            </div>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center" @click="get_campaigns('Elder Campaign')">
            <div class="font-bold px-5 py-3 cursor-pointer hover:bg-green-500 rounded-t-lg h-30 w-30"
              v-on:click="toggleTabs(9)"
              v-bind:class="{ 'bg-gray-300': openTab !== 9, 'rounded-t-lg bg-green-500': openTab === 9 }">
              <!-- <div class="text-gray-700 text-center bg-green-500 px-4 py-2 m-2"> -->
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/geriatrics.png" />Elder
              <!-- </div> -->
            </div>
          </li>
        </ul>
        <hr />
        <!-- <div class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded">
          <div class="px-4 py-5 flex-auto">
            <div class="tab-content tab-space overflow-y-auto h-40">
              <div v-bind:class="{ 'hidden': openTab !== 1, 'block': openTab === 1 }">

                {{ recent_donation }}
                <div>
                  {{ recent_donation }}
                </div>
              </div>
              <div v-bind:class="{ 'hidden': openTab !== 2, 'block': openTab === 2 }">
                <p>
                  {{ tab2 }}
                </p>
              </div>
            </div>
          </div>
        </div> -->
      </div>
    </div>




    <div class="grid lg:grid-cols-3 md:grid-cols-3 sm:grid-cols-2 gap-2">
      <div v-for="data in campaigns">
        <div class="p-10">
          <!--Card 1-->
          <div class="max-w-xs rounded overflow-hidden shadow-lg">
            <img class="w-full h-40 cursor-pointer" :src="data.campain_image" alt="Mountain" @click="donate(data.name)">
            <div class="py-4">
              <div class="font-bold text-green-500 text-xl mb-2 truncate">{{ data.short_description }}</div>
              <p class="text-gray-700 text-base truncate">
                By: {{ data.ngo }}
              <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700 mt-2">
                <div v-if="data.raised_amount" class="bg-green-500 h-2.5 rounded-full"
                  :style="{ width: data.raised_amount * 100 / data.donation_amount + '%' }"></div>
                <!-- <div v-if="data.raised_amount" class="bg-blue-600 h-2.5 rounded-full" style="width: 50%"></div> -->
              </div>
              <div class="flex justify-between mt-2 font-bold">
                <span>Raised: {{ data.raised_amount }}</span><span>Goal: {{ data.donation_amount }}</span>
              </div>
              </p>
            </div>
            <div class="px-6 pt-4 pb-2 flex justify-between">
              <button class="text-green-500">share</button>
              <button
                class="rounded-lg bg-green-500 text-white active:bg-green-600 font-bold uppercase text-sm px-6 py-3 shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                type="button" @click="donate(data.name)"> donate now </button>
            </div>
          </div>
        </div>

        <!-- <div class="flex justify-center">
        <div class="rounded-lg shadow-lg bg-white max-w-sm">
          <a href="#!">
            <img class="rounded-t-lg" :src="data.campain_image" alt="Mountain" @click="donate(data.name)"/>
          </a>
          <div class="p-6">
            <h5 class="text-gray-900 text-xl font-medium mb-2 truncate">{{ data.short_description }}</h5>
            <p class="text-gray-700 text-base mb-4">
              Some quick example text to build on the card title and make up the bulk of the card's
              content.
            </p>
            <button type="button" class=" inline-block px-6 py-2.5 bg-green-500 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Button</button>
          </div>
        </div>
      </div> -->


      </div>
    </div>

    <div class="text-center mt-10">
      <h2 class="text-4xl font-bold text-green-500 mb-2">Testimonials</h2>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet, voluptate!</p>
    </div>

    <div class="flex flex-wrap justify-center mt-5">
      <div class="">
        <ul class="flex mb-0 list-none flex-wrap pt-3 pb-4 flex-row">
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
            <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal cursor-pointer"
              v-on:click="toggleTabsTestimonials(1)"
              v-bind:class="{ 'bg-white': openTabTestimonials !== 1, 'bg-green-500 text-white': openTabTestimonials === 1 }">
              <i class="fas fa-space-shuttle text-base mr-1"></i> Celebrities
            </a>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
            <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal cursor-pointer"
              v-on:click="toggleTabsTestimonials(2)"
              v-bind:class="{ 'bg-white': openTabTestimonials !== 2, 'bg-green-500 text-white': openTabTestimonials === 2 }">
              <i class="fas fa-cog text-base mr-1"></i> Donors
            </a>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
            <a class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal cursor-pointer"
              v-on:click="toggleTabsTestimonials(3)"
              v-bind:class="{ 'bg-white': openTabTestimonials !== 3, 'bg-green-500 text-white': openTabTestimonials === 3 }">
              <i class="fas fa-cog text-base mr-1"></i> NGOs
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded">
      <div class="px-4 py-5 flex-auto">
        <div class="tab-content tab-space">
          <div v-bind:class="{ 'hidden': openTabTestimonials !== 1, 'block': openTabTestimonials === 1 }">
            <p>


            <div class="grid lg:grid-cols-3 md:grid-cols-3 sm:grid-cols-2 mt-20">
              <div class="flex flex-col min-w-0 break-words w-full mb-20 shadow-xl rounded-lg">
                <div class="px-6 bg-gray-500 rounded-lg lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="relative">
                        <img alt="..." src="../../src/assets/Inter/img/gpay.png"
                          class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-6 px-3 mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-center mt-12">
                    <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                      Jenna Stones
                    </h3>
                    <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                      <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                      Los Angeles, California
                    </div>
                    <div class="mb-2 text-blueGray-600 mt-10">
                      <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                      Solution Manager - Creative Tim Officer
                    </div>
                    <div class="mb-2 text-blueGray-600">
                      <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      University of Computer Science
                    </div>
                  </div>
                </div>
              </div>


              <div class="flex flex-col min-w-0 break-words w-full mb-20 shadow-xl rounded-lg">
                <div class="px-6 bg-gray-500 rounded-lg lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="relative">
                        <img alt="..." src="../../src/assets/Inter/img/phonepay.png"
                          class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-6 px-3 mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-center mt-12">
                    <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                      Jenna Stones
                    </h3>
                    <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                      <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                      Los Angeles, California
                    </div>
                    <div class="mb-2 text-blueGray-600 mt-10">
                      <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                      Solution Manager - Creative Tim Officer
                    </div>
                    <div class="mb-2 text-blueGray-600">
                      <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      University of Computer Science
                    </div>
                  </div>
                </div>
              </div>

              <div class="flex flex-col min-w-0 break-words w-full mb-20 shadow-xl rounded-lg">
                <div class="px-6 bg-gray-500 rounded-lg lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="relative">
                        <img alt="..." src="../../src/assets/Inter/img/gpay.png"
                          class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-6 px-3 mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-center mt-12">
                    <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                      Jenna Stones
                    </h3>
                    <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                      <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                      Los Angeles, California
                    </div>
                    <div class="mb-2 text-blueGray-600 mt-10">
                      <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                      Solution Manager - Creative Tim Officer
                    </div>
                    <div class="mb-2 text-blueGray-600">
                      <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      University of Computer Science
                    </div>
                  </div>
                </div>
              </div>
            </div>


            </p>
          </div>
          <div v-bind:class="{ 'hidden': openTabTestimonials !== 2, 'block': openTabTestimonials === 2 }">
            <p>


            <div class="grid lg:grid-cols-3 md:grid-cols-3 sm:grid-cols-2 mt-20">
              <div class="flex flex-col min-w-0 break-words w-full mb-20 shadow-xl rounded-lg">
                <div class="px-6 bg-gray-500 rounded-lg lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="relative">
                        <img alt="..." src="../../src/assets/Inter/img/gpay.png"
                          class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-6 px-3 mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-center mt-12">
                    <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                      Jenna Stones
                    </h3>
                    <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                      <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                      Los Angeles, California
                    </div>
                    <div class="mb-2 text-blueGray-600 mt-10">
                      <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                      Solution Manager - Creative Tim Officer
                    </div>
                    <div class="mb-2 text-blueGray-600">
                      <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      University of Computer Science
                    </div>
                  </div>
                </div>
              </div>


              <div class="flex flex-col min-w-0 break-words w-full mb-20 shadow-xl rounded-lg">
                <div class="px-6 bg-gray-500 rounded-lg lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="relative">
                        <img alt="..." src="../../src/assets/Inter/img/paytm.png"
                          class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-6 px-3 mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-center mt-12">
                    <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                      John Stones
                    </h3>
                    <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                      <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                      Los Angeles, California
                    </div>
                    <div class="mb-2 text-blueGray-600 mt-10">
                      <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                      Solution Manager - Creative Tim Officer
                    </div>
                    <div class="mb-2 text-blueGray-600">
                      <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      University of Computer Science
                    </div>
                  </div>
                </div>
              </div>

              <div class="flex flex-col min-w-0 break-words w-full mb-20 shadow-xl rounded-lg">
                <div class="px-6 bg-gray-500 rounded-lg lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="relative">
                        <img alt="..." src="../../src/assets/Inter/img/gpay.png"
                          class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-6 px-3 mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-center mt-12">
                    <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                      Jenna Abc
                    </h3>
                    <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                      <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                      Los Angeles
                    </div>
                    <div class="mb-2 text-blueGray-600 mt-10">
                      <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                      Solution Manager - Cresddsafdsfgfse Tim Officer
                    </div>
                    <div class="mb-2 text-blueGray-600">
                      <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      University of Computer Science
                    </div>
                  </div>
                </div>
              </div>
            </div>


            </p>
          </div>
          <div v-bind:class="{ 'hidden': openTabTestimonials !== 3, 'block': openTabTestimonials === 3 }">
            <p>


            <div class="grid lg:grid-cols-3 md:grid-cols-3 sm:grid-cols-2 mt-20">
              <div class="flex flex-col min-w-0 break-words w-full mb-20 shadow-xl rounded-lg">
                <div class="px-6 bg-gray-500 rounded-lg lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="relative">
                        <img alt="..." src="../../src/assets/Inter/img/gpay.png"
                          class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-6 px-3 mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-center mt-12">
                    <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                      Jenna Sto
                    </h3>
                    <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                      <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                      Los Angeles, California
                    </div>
                    <div class="mb-2 text-blueGray-600 mt-10">
                      <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                      Solution Manager - Creative Tim Officer
                    </div>
                    <div class="mb-2 text-blueGray-600">
                      <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      University
                    </div>
                  </div>
                </div>
              </div>


              <div class="flex flex-col min-w-0 break-words w-full mb-20 shadow-xl rounded-lg">
                <div class="px-6 bg-gray-500 rounded-lg lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="relative">
                        <img alt="..." src="../../src/assets/Inter/img/bhim.png"
                          class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-6 px-3 mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-center mt-12">
                    <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                      Jenna Sto
                    </h3>
                    <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                      <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                      Los Angeles, California
                    </div>
                    <div class="mb-2 text-blueGray-600 mt-10">
                      <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                      Solution Manager - Creative Tim Officer
                    </div>
                    <div class="mb-2 text-blueGray-600">
                      <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      University
                    </div>
                  </div>
                </div>
              </div>

              <div class="flex flex-col min-w-0 break-words w-full mb-20 shadow-xl rounded-lg">
                <div class="px-6 bg-gray-500 rounded-lg lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="relative">
                        <img alt="..." src="../../src/assets/Inter/img/gpay.png"
                          class="shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-6 px-3 mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-center mt-12">
                    <h3 class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2">
                      Jenna Sto
                    </h3>
                    <div class="text-sm leading-normal mt-0 mb-2 text-blueGray-400 font-bold uppercase">
                      <i class="fas fa-map-marker-alt mr-2 text-lg text-blueGray-400"></i>
                      Los Angeles, California
                    </div>
                    <div class="mb-2 text-blueGray-600 mt-10">
                      <i class="fas fa-briefcase mr-2 text-lg text-blueGray-400"></i>
                      Solution Manager - Creative Tim Officer
                    </div>
                    <div class="mb-2 text-blueGray-600">
                      <i class="fas fa-university mr-2 text-lg text-blueGray-400"></i>
                      University
                    </div>
                  </div>
                </div>
              </div>
            </div>

            </p>
          </div>
        </div>
      </div>
    </div>

    <div class="text-center mt-10">
      <h2 class="text-3xl font-bold text-green-500 mb-5">Featured in</h2>
    </div>
    <div class="grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 gap-2">

      <div class="flex flex-wrap">
        <div class="lg:flex lg:w-3/12 xl:w-3/12">
          <img src="../../src/assets/Inter/img/bhim.png" alt="f" class="rounded-full w-30 h-20" />
        </div>
        <div class="lg:w-9/12 xl:w-9/12">
          <div class="md:px-5">
            <h4 class="text-xl text-green-500">Protection</h4>
            <!-- <p class="font-semibold mb-4">Graphic designer</p> -->
            <p class="text-gray-500 mb-2">
              Lorem ipsum dolor sit.
            </p>
          </div>
        </div>
      </div>
      <div class="flex flex-wrap items-center">
        <div class="lg:flex lg:w-3/12 xl:w-3/12">
          <img src="../../src/assets/Inter/img/bhim.png" alt="f" class="rounded-full w-30 h-20" />
        </div>
        <div class="lg:w-9/12 xl:w-9/12">
          <div class="md:px-5">
            <h4 class="text-xl text-green-500">Prevention</h4>
            <!-- <p class="font-semibold mb-4">Graphic designer</p> -->
            <p class="text-gray-500 mb-2">
              Lorem ipsum dolor sit.
            </p>
          </div>
        </div>
      </div>
      <div class="flex flex-wrap">
        <div class="lg:flex lg:w-3/12 xl:w-3/12">
          <img src="../../src/assets/Inter/img/bhim.png" alt="f" class="rounded-full w-30 h-20" />
        </div>
        <div class="lg:w-9/12 xl:w-9/12">
          <div class="md:px-5">
            <h4 class="text-xl text-green-500">Treatments</h4>
            <!-- <p class="font-semibold mb-4">Graphic designer</p> -->
            <p class="text-gray-500 mb-2">
              Lorem ipsum dolor sit.
            </p>
          </div>
        </div>
      </div>
      <div class="flex flex-wrap">
        <div class="lg:flex lg:w-3/12 xl:w-3/12">
          <img src="../../src/assets/Inter/img/bhim.png" alt="f" class="rounded-full w-30 h-20" />
        </div>
        <div class="lg:w-9/12 xl:w-9/12">
          <div class="md:px-5">
            <h4 class="text-xl text-green-500">Symptoms</h4>
            <!-- <p class="font-semibold mb-4">Graphic designer</p> -->
            <p class="text-gray-500 mb-2">
              Lorem ipsum dolor sit.
            </p>
          </div>
        </div>
      </div>
    </div>


    <div class="text-center mt-10">
      <h2 class="text-3xl font-bold text-green-500 mb-2">Awards</h2>
    </div>
    <div class="grid lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2 gap-2 text-center">
      <div class="p-10">
        <!--Card 1-->
        <div class="max-w-sm rounded-lg overflow-hidden shadow-lg">
          <img class="w-full h-40 cursor-pointer"
            src="../../src/assets/Inter/img/icon/istockphoto-522640266-612x612.jpg" alt="Mountain"
            @click="donate(data.name)">
          <div class="py-4 text-gray-700">
            <div class="font-bold text-xl mb-2">zxcvzfgzx</div>
            <p class="text-base">
              National Business Excellence And Achievers Award 2021
            </p>
          </div>
        </div>
      </div>
      <div class="p-10">
        <!--Card 1-->
        <div class="max-w-sm rounded-lg overflow-hidden shadow-lg">
          <img class="w-full h-40 cursor-pointer"
            src="../../src/assets/Inter/img/icon/istockphoto-522640266-612x612.jpg" alt="Mountain"
            @click="donate(data.name)">
          <div class="py-4 text-gray-700">
            <div class="font-bold text-xl mb-2">zxcvzfgzx</div>
            <p class="text-base">
              National Business Excellence And Achievers Award 2021
            </p>
          </div>
        </div>
      </div>
      <div class="p-10">
        <!--Card 1-->
        <div class="max-w-sm rounded-lg overflow-hidden shadow-lg">
          <img class="w-full h-40 cursor-pointer"
            src="../../src/assets/Inter/img/icon/istockphoto-522640266-612x612.jpg" alt="Mountain"
            @click="donate(data.name)">
          <div class="py-4 text-gray-700">
            <div class="font-bold text-xl mb-2">zxcvzfgzx</div>
            <p class="text-base">
              National Business Excellence And Achievers Award 2021
            </p>
          </div>
        </div>
      </div>
      <div class="p-10">
        <!--Card 1-->
        <div class="max-w-sm rounded-lg overflow-hidden shadow-lg">
          <img class="w-full h-40 cursor-pointer"
            src="../../src/assets/Inter/img/icon/istockphoto-522640266-612x612.jpg" alt="Mountain"
            @click="donate(data.name)">
          <div class="py-4 text-gray-700">
            <div class="font-bold text-xl mb-2">zxcvzfgzx</div>
            <p class="text-base">
              National Business Excellence And Achievers Award 2021
            </p>
          </div>
        </div>
      </div>
    </div>



  </div>

  <!-- <div class="flex flex-wrap"> -->
  <!-- <div v-for="data in campaigns"> 
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
      <Button @click="viewmore(data.name)" appearance="primary">View More</Button>
      <button href="#">share</button>
      <button class="bg-emerald-500 text-white active:bg-emerald-600 font-bold uppercase text-sm px-6 py-3 shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" @click="donate(data.name)"> donate now </button>
        <Button @click="donate(data.name)" appearance="danger">Donate</Button>
    </div>
  </div> -->
  <!-- </div> -->
  <!-- ////////////////// -->



  <!-- ///////////////// -->
  <Footer />
</template>

<script>
import axios from 'axios';
import Navbar from "../components/Navbar.vue";
import Footer from "../components/Footer.vue";
import { inject, provide, ref } from "vue"

export default {
  name: 'Home',
  created() {
    this.get_campaigns()
  },
  components: {
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
      campaigns: [],
      loading: false,
      selection: 1,
      openTab: 1,
      openTabTestimonials: 1,

    }
  },
  resources: {
    // get_data(){
    //   return{
    //     method: '/api/method/sadbhavna_donatekart.api.api.get_campaign_details',
    //     onSuccess(){
    //       console.log("Success")
    //     },
    //     onError(){
    //       console.log("Error")
    //     }
    //   }
    // }
  },
  methods: {
    toggleTabs: function (tabNumber) {
      this.openTab = tabNumber
    },
    toggleTabsTestimonials: function (tabNumber) {
      this.openTabTestimonials = tabNumber
    },
    get_campaigns(category) {
      let url = ''
      if (category == null) {
        url = '/api/resource/Donation Campaign?filters={"published": 1}&fields=["name", "campain_image", "campaign_title", "donation_amount", "raised_amount", "start_date", "end_date", "short_description", "ngo", "campaign_category"]'
      }
      else {
        url = `/api/resource/Donation%20Campaign?filters=[["Donation Campaign","campaign_category","=","${category}"],["Donation Campaign","published","=",1]]&fields=["name", "campain_image", "campaign_title", "donation_amount", "raised_amount", "start_date", "end_date", "short_description", "ngo", "campaign_category"]`
      }
      axios.get(url).then((response) => {
        // console.log("campaign", response)
        this.campaigns = response.data['data']
      }).catch(function (error) {
        console.log(error);
      })
    },
    reserve() {
      this.loading = true
      setTimeout(() => (this.loading = false), 2000)
    },
    viewmore(name) {
      this.$router.push(`/sadbhavna/campaign-donation/${name}`)
    },
    donate(name) {
      // this.$router.push(`/sadbhavna/donate/${name}`)
      this.$router.push(`/sadbhavna/campaign-donation/${name}`)
    }
  },
  // mounted(){
  //   if (!this.user.isLoggedIn()) {
  // 		this.$router.push({
  // 			name: "DeskLogin",
  // 			query: { route: this.$route.path },
  // 		})
  // 		return
  // 	}
  //   // else{
  //   //   this.$router.push(`/sadbhavna/login`) 
  //   // }
  // 	if (!this.user.has_desk_access) {
  // 		this.$router.push({ path: "/home" })
  // 		return
  // 	}
  // }

  // beforeMount(){
  //   this.get_campaign
  // }
}

</script>
