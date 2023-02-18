<template>


  <!-- Header-->

  <div class="bg-no-repeat  bg-cover bg-center "
    style="background-image: url('../../src/assets/Inter/img/Frame1.jpg')">
      <Navbar />
    <div class="container mx-auto h-full">
      <div class="grid lg:grid-cols-2 pb-10 m-10">

        <div class="lg:pt-52 sm:pt-4 pr-0 lg:pr-10 tracking-wide">
          <p class="text-[#40b751] font-sans text-center lg:text-left font-semibold leading-tight text-[28px] md:text-[40px] lg:text-[43px] [text-shadow:_0_1px_0_rgb(0_0_0_/_40%)]">
            Donate with 
            <span class="text-gray-700">100% Transparency</span>
            on
            <span class="text-gray-700">most trusted</span>
            crowd funding platform of India.
          </p>
        </div>
        <div class="md:pl-48 lg:pl-0 pl-16 lg:pt-0 pt-8 ">
          <img src="../../src/assets/Inter/img/map2.png" class="h-48 md:h-80 lg:h-full w-48 md:w-80 lg:w-full" />
        </div>
      </div>
    </div>
  </div>



<!----------------------------------------->
    
    <div class="container mx-auto h-full sm:p-4 lg:p-16 -mt-16 lg:-mt-32 pl-4 lg:pl-0 pr-4 lg:pr-0">
<div class="">
  <div class="bg-white rounded-xl shadow-lg">
  <div class="grid p-5 sm:grid-cols-1 md:grid-cols-4 lg:grid-cols-4 gap-8">
    <div class="md:col-span-2 lg:col-span-1">
      <img class="pl-3 pt-3 pb-1 md:h-80 lg:h-56 sm:w-full md:w-96 lg:w-96" src="../../src/assets/Inter/img/Old-Lady.png" alt="" />
    </div>
    <div class="md:col-span-2 lg:col-span-3 pr-0 lg:pr-16">
      <button class="bg-[#364958] text-base rounded-lg pl-4 pr-4 pt-2 pb-2 text-white mb-2 md:mt-3">Featured</button>
      <h5 class="text-[#364958] text-2xl font-medium mb-2">This Australian Has Made India His Home To Feed Hundreds Of
            Poor People, Help Him</h5>
      <p class="text-[#364958]">
            In a world that has seen a lot of pain and suffering, The Lot wishes to bring back the smiles on helpless
            faces. You can join their mission.
      </p>
          <a class="" href="#"><p class="text-[#40b751] pt-3 font-bold">Donate Now</p></a>
    </div>
  </div>
  </div>
</div>



    <!-- Categories -->

    
    <div class="text-center mt-10">
      <h2 class="text-3xl font-bold text-[#40b751] mb-2">Categories</h2>
      <p class="text-[#364958]">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet, voluptate!</p>
    </div>



    <div class="flex mt-3 border-b mr-12 ">
      <div class="overflow-x-auto">
        <ul class="flex mb-0 list-none pt-3 pb-0 overflow-y-hidden lg:overflow-x-hidden ">
          <li class="-mb-px mr-3 last:mr-0 text-center" @click="get_campaigns()">
            <div class="font-bold px-10 py-2 cursor-pointer hover:bg-[#40b751] hover:text-white border rounded-t-3xl border-gray-200 h-30 w-30"
              v-on:click="toggleTabs(1)"
              v-bind:class="{ 'bg-white text-gray-500': openTab !== 1, 'rounded-t-3xl bg-[#40b751] text-white': openTab === 1 }">
             
              <div class="grid justify-items-center" v-if="openTab !== 1">
                <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/grid (2).png" />All
              </div>
              <div class="grid justify-items-center" v-else="openTab === 1">
                <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/grid.png" />All
              </div>
              
              
            </div>           
          </li>
          
          <li class="-mb-px mr-3 last:mr-0 text-center" @click="get_campaigns('Animal Campaign')">
            <div class="font-bold px-8 py-2 cursor-pointer hover:bg-[#40b751] hover:text-white border rounded-t-3xl border-gray-200 h-30 w-30"
              v-on:click="toggleTabs(2)"
              v-bind:class="{ 'bg-white text-gray-500': openTab !== 2, 'rounded-t-3xl bg-[#40b751] text-white': openTab === 2 }">
              
              <div class="grid justify-items-center" v-if="openTab !== 2">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/paw (1).png" />Animal
              </div>
              <div class="grid justify-items-center" v-else="openTab === 2">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/paw.png" />Animal
              </div>
              
             
            </div>
          </li>
        
          <li class="-mb-px mr-3 last:mr-0 flex-auto text-center" @click="get_campaigns('Education Campaign')">
            <div class="font-bold px-6 py-2 cursor-pointer  hover:bg-[#40b751] hover:text-white border rounded-t-3xl border-gray-200 h-30 w-30"
              v-on:click="toggleTabs(3)"
              v-bind:class="{ 'bg-white text-gray-500': openTab !== 3, 'rounded-t-3xl bg-[#40b751] text-white': openTab === 3 }">
              
              <div class="grid justify-items-center" v-if="openTab !== 3">
              <img class="h-10 w-10 " src="../../src/assets/Inter/img/icon/mortarboard (1).png" />Education 
              </div>
              <div class="grid justify-items-center" v-else="openTab === 3">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/mortarboard.png" />Education
              </div>
              
              
            </div>
          </li>
          <li class="-mb-px mr-3 last:mr-0 flex-auto text-center" @click="get_campaigns('Children Campaign')">
            <div class="font-bold px-8 py-2 cursor-pointer hover:bg-[#40b751] hover:text-white border rounded-t-3xl border-gray-200 h-30 w-30"
              v-on:click="toggleTabs(4)"
              v-bind:class="{ 'bg-white text-gray-500': openTab !== 4, 'rounded-t-3xl bg-[#40b751] text-white': openTab === 4 }">
              
              <div class="grid justify-items-center" v-if="openTab !== 4">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/children (1).png" />Children
              </div>
              <div class="grid justify-items-center" v-else="openTab === 4">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/children.png" />Children
              </div>
              
              
            </div>
          </li>
          <li class="-mb-px mr-3 last:mr-0 flex-auto text-center" @click="get_campaigns('Medical Campaign')">
            <div class="font-bold px-8 py-2 cursor-pointer hover:bg-[#40b751] hover:text-white border rounded-t-3xl border-gray-200 h-30 w-30"
              v-on:click="toggleTabs(5)"
              v-bind:class="{ 'bg-white text-gray-500': openTab !== 5, 'rounded-t-3xl bg-[#40b751] text-white': openTab === 5 }">
              
              <div class="grid justify-items-center" v-if="openTab !== 5">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/healthcare (1).png" />Medical
              </div>
              <div  class="grid justify-items-center"  v-else="openTab === 5">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/healthcare.png" />Medical
              </div>
              
              
            </div>
          </li>
          <li class="-mb-px mr-3 last:mr-0 flex-auto text-center" @click="get_campaigns('Hunger Campaign')">
            <div class="font-bold px-8 py-2 cursor-pointer hover:bg-[#40b751] hover:text-white border rounded-t-3xl border-gray-200 h-30 w-30"
              v-on:click="toggleTabs(6)"
              v-bind:class="{ 'bg-white text-gray-500': openTab !== 6, 'rounded-t-3xl bg-[#40b751] text-white': openTab === 6 }">
             
              <div class="grid justify-items-center" v-if="openTab !== 6">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/supplies (1).png" />Hunger
              </div>
              <div class="grid justify-items-center" v-else="openTab === 6">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/supplies.png" />Hunger                
              </div>
              
            </div>
          </li>
          <li class="-mb-px mr-3 last:mr-0 flex-auto text-center" @click="get_campaigns('Religiouse Campaign')">
            <div class="font-bold px-5 py-2 cursor-pointer hover:bg-[#40b751] hover:text-white border rounded-t-3xl border-gray-200 h-30 w-30"
              v-on:click="toggleTabs(7)"
              v-bind:class="{ 'bg-white text-gray-500': openTab !== 7, 'rounded-t-3xl bg-[#40b751] text-white': openTab === 7 }">
              
              <div class="grid justify-items-center" v-if="openTab !== 7">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/pray (1).png" />Religiouse
              </div>
              <div class="grid justify-items-center" v-else="openTab === 7">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/pray.png" />Religiouse
              </div>
              
              
            </div>
          </li>
          <li class="-mb-px mr-3 last:mr-0 flex-auto text-center" @click="get_campaigns('Disability Campaign')">
            <div class="font-bold px-6 py-2 cursor-pointer hover:bg-[#40b751] hover:text-white border rounded-t-3xl border-gray-200 h-30 w-30"
              v-on:click="toggleTabs(8)"
              v-bind:class="{ 'bg-white text-gray-500': openTab !== 8, 'rounded-t-3xl bg-[#40b751] text-white': openTab === 8 }">
              
              <div class="grid justify-items-center" v-if="openTab !== 8">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/disability (1).png" />Disability
              </div>
              <div class="grid justify-items-center" v-else="openTab === 8">
              <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/disability.png" />Disability
              </div>
              
             
            </div>
          </li>
          <li class="-mb-px mr-3 last:mr-0 flex-auto text-center" @click="get_campaigns('Elder Campaign')">
            <div class="font-bold px-9 py-2 cursor-pointer hover:bg-[#40b751] hover:text-white border rounded-t-3xl border-gray-200 h-30 w-30"
              v-on:click="toggleTabs(9)"
              v-bind:class="{ 'bg-white text-gray-500': openTab !== 9, 'rounded-t-3xl bg-[#40b751] text-white': openTab === 9 }">
              
              <div class="grid justify-items-center" v-if="openTab !== 9">
                <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/old-man (1).png" />Elder
              </div>
              <div class="grid justify-items-center" v-else="openTab === 9">
                <img class="h-10 w-10" src="../../src/assets/Inter/img/icon/old-man.png" />Elder
              </div>
              
            </div>
          </li>
        </ul>
     
      </div>
    </div>


<!--Cards-->
    <div class="grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-0 md:gap-6 lg:gap-0">
      <div v-for="data in campaigns">
        <div class="pb-5 md:pb-10 lg:pb-10 pt-5 md:pt-4 lg:pt-10 ">
          <div class="max-w-[350px] md:max-w-[350px] lg:max-w-sm rounded overflow-hidden shadow-lg">
            <img class="w-full h-40 cursor-pointer" :src="data.campain_image" alt="Mountain" @click="donate(data.name)">
            <div class="pt-9 pr-9 pd-7 pl-9 ">
              <div class="font-medium text-[#40b751] text-xl mb-2 truncate">Help us to Send Food{{ data.short_description }}</div>
              <p class="text-gray-700 text-base truncate">
                By: {{ data.ngo }}
              <div class="w-full bg-gray-200 rounded h-3.5 dark:bg-gray-700 mt-6 mb-6 ">
                <div v-if="data.raised_amount" class="bg-[#40b751] h-3.5 rounded"
                  :style="{ width: data.raised_amount * 100 / data.donation_amount + '%' }"></div>
                
              </div>
              <div class="flex border-b-2 border-b-gray-100  justify-between mt-6 mb-6 pb-6 text-sm font-bold">
                <span>Raised: {{ data.raised_amount }}</span><span>Goal: {{ data.donation_amount }}</span>
              </div>
              </p>
            </div>
            <div class="sm:pr-9 md:pr-2 lg:pr-9 pb-7 pl-9 flex justify-between">
              <button class="text-[#40b751] text-base">Share</button>
              <button
                class="rounded-lg bg-[#40b751] hover:bg-white text-white hover:border-[#40b751] hover:border hover-border-solid hover:text-[#40b751] active:bg-green-600 uppercase text-xs md:text-xs lg:text-sm px-6 py-3 shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                type="button" @click="donate(data.name)"> donate now </button>
            </div>
          </div>
        </div>
        </div>
      </div>
      </div>

    <!--Testimonials-->

    <div class="bg-[#ebf8ec]">
    <div class="container mx-auto h-full">
    <div class="text-center mt-10">
      <h2 class="text-3xl pt-20 font-black text-[#40b751] mb-2">Testimonials</h2>
      <p class="text-[#364958] text-[15px] font-light">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet, voluptate!</p>
    </div>


   
    <div class="flex border-b-2 ml-4 mr-8 border-b-solid border-gray-200 flex-wrap justify-center mt-5">
      <div class="grid ">
        <ul class="flex mb-0 list-none flex-wrap pt-3 flex-row">
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
            <a class="text-[16px] hover:border hover-border-100 font-xtralight  px-[12px] md:px-[20px] lg:px-[40px] py-[10px] md:py-[10px] lg:py-[12px] rounded block leading-normal cursor-pointer"
              v-on:click="toggleTabsTestimonials(1)"
              v-bind:class="{ 'bg-white': openTabTestimonials !== 1, 'bg-[#40b751] text-white': openTabTestimonials === 1 }">
              <i class="fas fa-space-shuttle text-base mr-1"></i> Celebrities
            </a>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
            <a class="text-[16px] hover:border hover-border-100 font-xtralight  px-[12px] md:px-[20px] lg:px-[40px] py-[10px] md:py-[10px] lg:py-[12px] rounded block leading-normal cursor-pointer"
              v-on:click="toggleTabsTestimonials(2)"
              v-bind:class="{ 'bg-white': openTabTestimonials !== 2, 'bg-[#40b751] text-white': openTabTestimonials === 2 }">
              <i class="fas fa-cog text-base mr-1"></i> Donors
            </a>
          </li>
          <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
            <a class="text-[16px] hover:border hover-border-100 font-xtralight px-[16px] md:px-[28px] lg:px-[48px] py-[10px] md:py-[10px] lg:py-[12px] rounded block leading-normal cursor-pointer"
              v-on:click="toggleTabsTestimonials(3)"
              v-bind:class="{ 'bg-white': openTabTestimonials !== 3, 'bg-[#40b751] text-white': openTabTestimonials === 3 }">
              <i class="fas fa-cog text-base mr-1"></i> NGOs
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="flex flex-col min-w-0 break-words w-full">
      <div class=" px-4 py-5 flex-auto">
        <div class="tab-content tab-space">
          <div v-bind:class="{ 'hidden': openTabTestimonials !== 1, 'block': openTabTestimonials === 1 }">
            <p>
            <div class="grid lg:grid-cols-3  md:grid-cols-1 sm:grid-cols-1 mt-20">
              <div class="flex h-[440px] flex-col min-w-0 break-words w-full sm:mb-0 md:mb-2 lg:mb-10 ">
                <div class="px-6 h-3/4 md:h-4/6 lg:h-full overflow-scroll overflow-x-hidden shadow-xl shadow-[rgb(0 0 0 / 5%)] bg-white lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="absolute">
                        <img alt="..." src="../../src/assets/Inter/img/person_1.jpg"
                          class=" rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 object-center max-w-100-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-8 px-3 mt-0 md:mt-0 lg:mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-left mt-0 pb-0">
                    <h3 class="text-[20px] md:text-[22px] lg:text-[24px] leading-normal mb-0 text-gray-600 ">
                      Name Tab 1
                    </h3>
                    <div class="text-[12px] md:text-[14px] lg:text-[16px] leading- normal mt-0 text-[#364958] text-opacity-60 ">
                      <i class="fas fa-map-marker-alt text-lg text-blueGray-400"></i>
                      Designation
                    </div>
                    <div class="text-[14px] md:text-[18px] lg:text-[18px] leading-8 text-blueGray-600 mt-4 ">
                      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
                      the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
                      type and scrambled it to make a type specimen book. 
                    </div>
                    
                  </div>
                </div>
              </div>


             <div class="flex h-[440px] flex-col min-w-0 break-words w-full sm:mb-0 md:mb-2 lg:mb-10 ">
                <div class="px-6 h-3/4 md:h-4/6 lg:h-full overflow-scroll overflow-x-hidden shadow-xl shadow-[rgb(0 0 0 / 5%)] bg-white lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="absolute">
                        <img alt="..." src="../../src/assets/Inter/img/person_1.jpg"
                          class=" rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 object-center max-w-100-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-8 px-3 mt-0 md:mt-0 lg:mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-left mt-0 pb-0">
                    <h3 class="text-[20px] md:text-[22px] lg:text-[24px] leading-normal mb-0 text-gray-600 ">
                      Name Tab 1
                    </h3>
                    <div class="text-[12px] md:text-[14px] lg:text-[16px] leading- normal mt-0 text-[#364958] text-opacity-60 ">
                      <i class="fas fa-map-marker-alt text-lg text-blueGray-400"></i>
                      Designation
                    </div>
                    <div class="text-[14px] md:text-[18px] lg:text-[18px] leading-8 text-blueGray-600 mt-4 ">
                      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
                      the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
                      type and scrambled it to make a type specimen book. 
                    </div>
                    
                  </div>
                </div>
              </div>

              <div class="flex h-[440px] flex-col min-w-0 break-words w-full sm:mb-0 md:mb-2 lg:mb-10 ">
                <div class="px-6 h-3/4 md:h-4/6 lg:h-full overflow-scroll overflow-x-hidden shadow-xl shadow-[rgb(0 0 0 / 5%)] bg-white lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="absolute">
                        <img alt="..." src="../../src/assets/Inter/img/person_1.jpg"
                          class=" rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 object-center max-w-100-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-8 px-3 mt-0 md:mt-0 lg:mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-left mt-0 pb-0">
                    <h3 class="text-[20px] md:text-[22px] lg:text-[24px] leading-normal mb-0 text-gray-600 ">
                      Name Tab 1
                    </h3>
                    <div class="text-[12px] md:text-[14px] lg:text-[16px] leading- normal mt-0 text-[#364958] text-opacity-60 ">
                      <i class="fas fa-map-marker-alt text-lg text-blueGray-400"></i>
                      Designation
                    </div>
                    <div class="text-[14px] md:text-[18px] lg:text-[18px] leading-8 text-blueGray-600 mt-4 ">
                      Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                    </div>
                    
                  </div>
                </div>
              </div>
            </div>


            </p>
          </div>
          <div v-bind:class="{ 'hidden': openTabTestimonials !== 2, 'block': openTabTestimonials === 2 }">
            <p>


            <div class="grid lg:grid-cols-3  md:grid-cols-1 sm:grid-cols-1 mt-20">
              <div class="flex h-[440px] flex-col min-w-0 break-words w-full sm:mb-0 md:mb-2 lg:mb-10 ">
                <div class="px-6 h-3/4 md:h-4/6 lg:h-full overflow-scroll overflow-x-hidden shadow-xl shadow-[rgb(0 0 0 / 5%)] bg-white lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="absolute">
                        <img alt="..." src="../../src/assets/Inter/img/person_1.jpg"
                          class=" rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 object-center max-w-100-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-8 px-3 mt-0 md:mt-0 lg:mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-left mt-0 pb-0">
                    <h3 class="text-[20px] md:text-[22px] lg:text-[24px] leading-normal mb-0 text-gray-600 ">
                      Name Tab 2
                    </h3>
                    <div class="text-[12px] md:text-[14px] lg:text-[16px] leading- normal mt-0 text-[#364958] text-opacity-60 ">
                      <i class="fas fa-map-marker-alt text-lg text-blueGray-400"></i>
                      Designation
                    </div>
                    <div class="text-[14px] md:text-[18px] lg:text-[18px] leading-8 text-blueGray-600 mt-4 ">
                      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
                      the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
                      type and scrambled it to make a type specimen book. It has survived not only five centuries, but
                      also the leap into electronic typesetting, remaining essentially unchanged.  
                    </div>
                    
                  </div>
                </div>
              </div>


             <div class="flex h-[440px] flex-col min-w-0 break-words w-full sm:mb-0 md:mb-2 lg:mb-10 ">
                <div class="px-6 h-3/4 md:h-4/6 lg:h-full overflow-scroll overflow-x-hidden shadow-xl shadow-[rgb(0 0 0 / 5%)] bg-white lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="absolute">
                        <img alt="..." src="../../src/assets/Inter/img/person_1.jpg"
                          class=" rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 object-center max-w-100-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-8 px-3 mt-0 md:mt-0 lg:mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-left mt-0 pb-0">
                    <h3 class="text-[20px] md:text-[22px] lg:text-[24px] leading-normal mb-0 text-gray-600 ">
                      Name Tab 2
                    </h3>
                    <div class="text-[12px] md:text-[14px] lg:text-[16px] leading- normal mt-0 text-[#364958] text-opacity-60 ">
                      <i class="fas fa-map-marker-alt text-lg text-blueGray-400"></i>
                      Designation
                    </div>
                    <div class="text-[14px] md:text-[18px] lg:text-[18px] leading-8 text-blueGray-600 mt-4 ">
                      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
                      the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
                      type and scrambled it to make a type specimen book. It has survived not only five centuries, but
                      also the leap into electronic typesetting, remaining essentially unchanged. 
                    </div>
                    
                  </div>
                </div>
              </div>

              <div class="flex h-[440px] flex-col min-w-0 break-words w-full sm:mb-0 md:mb-2 lg:mb-10 ">
                <div class="px-6 h-3/4 md:h-4/6 lg:h-full overflow-scroll overflow-x-hidden shadow-xl shadow-[rgb(0 0 0 / 5%)] bg-white lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="absolute">
                        <img alt="..." src="../../src/assets/Inter/img/person_1.jpg"
                          class=" rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 object-center max-w-100-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-8 px-3 mt-0 md:mt-0 lg:mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-left mt-0 pb-0">
                    <h3 class="text-[20px] md:text-[22px] lg:text-[24px] leading-normal mb-0 text-gray-600 ">
                      Name Tab 2
                    </h3>
                    <div class="text-[12px] md:text-[14px] lg:text-[16px] leading- normal mt-0 text-[#364958] text-opacity-60 ">
                      <i class="fas fa-map-marker-alt text-lg text-blueGray-400"></i>
                      Designation
                    </div>
                    <div class="text-[14px] md:text-[18px] lg:text-[18px] leading-8 text-blueGray-600 mt-4 ">
                     Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
                      the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
                      type and scrambled it to make a type specimen book. It has survived not only five centuries, but
                      also the leap into electronic typesetting, remaining essentially unchanged. 
                    </div>
                    
                  </div>
                </div>
              </div>
            </div>


            </p>
          </div>
          <div v-bind:class="{ 'hidden': openTabTestimonials !== 3, 'block': openTabTestimonials === 3 }">
            <p>


           <div class="grid lg:grid-cols-3  md:grid-cols-1 sm:grid-cols-1 mt-20">
              <div class="flex h-[440px] flex-col min-w-0 break-words w-full sm:mb-0 md:mb-2 lg:mb-10 ">
                <div class="px-6 h-3/4 md:h-4/6 lg:h-full overflow-scroll overflow-x-hidden shadow-xl shadow-[rgb(0 0 0 / 5%)] bg-white lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="absolute">
                        <img alt="..." src="../../src/assets/Inter/img/person_1.jpg"
                          class=" rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 object-center max-w-100-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-8 px-3 mt-0 md:mt-0 lg:mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-left mt-0 pb-0">
                    <h3 class="text-[20px] md:text-[22px] lg:text-[24px] leading-normal mb-0 text-gray-600 ">
                      Name Tab 3
                    </h3>
                    <div class="text-[12px] md:text-[14px] lg:text-[16px] leading- normal mt-0 text-[#364958] text-opacity-60 ">
                      <i class="fas fa-map-marker-alt text-lg text-blueGray-400"></i>
                      Designation
                    </div>
                    <div class="text-[14px] md:text-[18px] lg:text-[18px] leading-8 text-blueGray-600 mt-4 ">
                      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
                      the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
                      type and scrambled it to make a type specimen book. It has survived not only five centuries, but
                      also the leap into electronic typesetting, remaining essentially unchanged. 
                    </div>
                    
                  </div>
                </div>
              </div>


             <div class="flex h-[440px] flex-col min-w-0 break-words w-full sm:mb-0 md:mb-2 lg:mb-10 ">
                <div class="px-6 h-3/4 md:h-4/6 lg:h-full overflow-scroll overflow-x-hidden shadow-xl shadow-[rgb(0 0 0 / 5%)] bg-white lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="absolute">
                        <img alt="..." src="../../src/assets/Inter/img/person_1.jpg"
                          class=" rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 object-center max-w-100-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-8 px-3 mt-0 md:mt-0 lg:mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-left mt-0 pb-0">
                    <h3 class="text-[20px] md:text-[22px] lg:text-[24px] leading-normal mb-0 text-gray-600 ">
                      Name Tab 3
                    </h3>
                    <div class="text-[12px] md:text-[14px] lg:text-[16px] leading- normal mt-0 text-[#364958] text-opacity-60 ">
                      <i class="fas fa-map-marker-alt text-lg text-blueGray-400"></i>
                      Designation
                    </div>
                    <div class="text-[14px] md:text-[18px] lg:text-[18px] leading-8 text-blueGray-600 mt-4 ">
                      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
                      the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
                      type and scrambled it to make a type specimen book. It has survived not only five centuries, but
                      also the leap into electronic typesetting, remaining essentially unchanged. 
                    </div>
                    
                  </div>
                </div>
              </div>

              <div class="flex h-[440px] flex-col min-w-0 break-words w-full sm:mb-0 md:mb-2 lg:mb-10 ">
                <div class="px-6 h-3/4 md:h-4/6 lg:h-full overflow-scroll overflow-x-hidden shadow-xl shadow-[rgb(0 0 0 / 5%)] bg-white lg:mr-6 md:mr-6">
                  <div class="flex flex-wrap justify-center">
                    <div class="w-full lg:w-3/12 px-4 lg:order-2 flex justify-center">
                      <div class="absolute">
                        <img alt="..." src="../../src/assets/Inter/img/person_1.jpg"
                          class=" rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 object-center max-w-100-px" />
                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center">
                      <div class="py-8 px-3 mt-0 md:mt-0 lg:mt-32 sm:mt-0">

                      </div>
                    </div>
                    <div class="w-full lg:w-4/12 px-4 lg:order-1">

                    </div>
                  </div>
                  <div class="text-left mt-0 pb-0">
                    <h3 class="text-[20px] md:text-[22px] lg:text-[24px] leading-normal mb-0 text-gray-600 ">
                      Name Tab 3
                    </h3>
                    <div class="text-[12px] md:text-[14px] lg:text-[16px] leading- normal mt-0 text-[#364958] text-opacity-60 ">
                      <i class="fas fa-map-marker-alt text-lg text-blueGray-400"></i>
                      Designation
                    </div>
                    <div class="text-[14px] md:text-[18px] lg:text-[18px] leading-8 text-blueGray-600 mt-4 ">
                      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
                      the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of
                      type and scrambled it to make a type specimen book. It has survived not only five centuries, but
                      also the leap into electronic typesetting, remaining essentially unchanged. 
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

    </div>
    </div>


<!--Featured In-->
    
    <div class="container mx-auto h-full">
    <div class="text-center mt-10">
      <h2 class="text-[24px] md:text-[24px] lg:text-[30px] font-bold text-[#40b751] mb-[20px]">Featured in</h2>
    </div>

    <div class="grid sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-4 ">
      <div class="flex pb-[34px] md:pb-[20px] lg:pb-[34px] ">
        <div class="">
        <img class="h-[46px] md:h-[50px] lg:h-[48px] w-[40px] md:w-[50px] lg:w-[40px] mr-3 ml-8 md:ml-0 lg:ml-0 pt-2" src="../../src/assets/Inter/img/protection.png" />
        </div>
        <div class="lg:w-9/12 xl:w-9/12">
          <p class="text-[16px] text-[#40b751] font-black">Protection</p>
          <p class="text-[#aaa]">Lorem ipsum dolor sit.</p>
        </div>
      </div>

      <div class="flex pb-[34px] md:pb-[20px] lg:pb-[0px]">
        <div class="">
        <img class="h-[46px] md:h-[50px] lg:h-[48px] w-[40px] md:w-[50px] lg:w-[40px] mr-3 ml-8 md:ml-0 lg:ml-0 pt-2" src="../../src/assets/Inter/img/mask.png" />
        </div>
        <div class="lg:w-9/12 xl:w-9/12">
        <p class="text-[16px] text-[#40b751] font-black">Prevention</p>
        <p class="text-[#aaa]">Lorem ipsum dolor sit.</p>
      </div>
    </div>

    <div class="flex pb-[34px] md:pb-[20px] lg:pb-[0px]">
      <div class="">
        <img class="h-[46px] md:h-[50px] lg:h-[48px] w-[40px] md:w-[50px] lg:w-[40px] mr-3 ml-8 md:ml-0 lg:ml-0 pt-2" src="../../src/assets/Inter/img/sanitizer.png" />
        </div>
        <div class="lg:w-9/12 xl:w-9/12">
        <p class="text-[16px] text-[#40b751] font-black">Treatments</p>
        <p class="text-[#aaa]">Lorem ipsum dolor sit.</p>
      </div>
      </div>

      <div class="flex pb-[34px] md:pb-[20px] lg:pb-[0px] ">
        <div class="">
        <img class="h-[46px] md:h-[50px] lg:h-[48px] w-[40px] md:w-[50px] lg:w-[40px] mr-3 ml-8 md:ml-0 lg:ml-0 pt-2" src="../../src/assets/Inter/img/virus.png" />
        </div>
        <div class="lg:w-9/12 xl:w-9/12">
        <p class="text-[16px] text-[#40b751] font-black">Symptoms</p>
        <p class="text-[#aaa]">Lorem ipsum dolor sit.</p>
      </div>
    </div>
    
   </div>
</div>
   <!--Awards-->

   <div class="bg-[#f5f3ff]">
       <div class="container mx-auto h-full">

    <div class="text-center mt-10">
      <h2 class="text-3xl font-bold text-[#40b751] pt-12">Awards</h2>
    </div>
    <div class="pb-16">
    <div class="grid lg:grid-cols-5 md:grid-cols-3 sm:grid-cols-1 gap-2 text-center">
      <div>
        <img class="px-24 md:px-8 py-8 lg:py-8 h-52 w-96" src="../../src/assets/Inter/img/images.png">
        <div>
          <p class="text-[#364958] font-medium text-[20px]">National Business Excellence And Achievers Award</p>
          <p class="text-[#364958] font-medium pt-2">2021</p>
        </div>
      </div>

      <div>
        <img class="px-24 md:px-8 py-8 lg:py-8 h-52 w-96" src="../../src/assets/Inter/img/images.png">
        <div>
          <p class="text-[#364958] font-medium text-[20px]">Top Ten Startups In Hyderabad</p>
          <p class="text-[#364958] font-medium pt-2">2020</p>
        </div>
      </div>

      <div>
        <img class="px-24 md:px-8 py-8 lg:py-8 h-52 w-96" src="../../src/assets/Inter/img/images.png">
        <div>
          <p class="text-[#364958] font-medium text-[20px]">Social Enterprise Challenge Award</p>
          <p class="text-[#364958] font-medium pt-2">2018</p>
        </div>
      </div>

      <div>
        <img class="px-24 md:px-8 py-8 lg:py-8 h-52 w-96" src="../../src/assets/Inter/img/images.png">
        <div>
          <p class="text-[#364958] font-medium text-[20px]">NASSCOM Social Innovation Award</p>
          <p class="text-[#364958] font-medium pt-2">2018</p>
        </div>
      </div>

      <div>
        <img class="px-24 md:px-8 py-8 lg:py-8 h-52 w-96" src="../../src/assets/Inter/img/images.png">
        <div>
          <p class="text-[#364958] font-medium text-[20px]">Indian Express 40 Under 40</p>
          <p class="text-[#364958] font-medium pt-2">2021</p>
        </div>
      </div>
      </div>
    </div>
  </div>
</div>

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
