<template>
  <div class="main-inner">
    <div class="hero-section">
      <div class="hero-section-inner row col-12 m-0 align-items-center">
        <div class="col-md-6">
          <div class="content col-md-8 mx-auto text-start" data-aos="fade-right" data-aos-delay="500">
            <h1><b style="color: #ff4a00">Our Pricing</b></h1>
            <div class="text-small mt-4">
              <span>Pick a plan that best fits your need</span>
            </div>
          </div>
        </div>
        <div class="col-md-5">
          <div class="image" data-aos="fade-left" data-aos-delay="300">
            <img src="@/assets/static/images/finance.png" alt="" class="img-fluid" />
          </div>
        </div>
      </div>
    </div>
    <div class="padding-giver">
      <div class="container p-0">
        <!-- section five -->
        <section class="five">
          <div class="title-wrapper">
            <div class="section-title">
              <h3>PRICING FOR EVERYONE</h3>
            </div>
            <div class="button-wrapper">
              <button class="active">Pay Monthly</button><button>Pay yearly (save 25%)</button>
            </div>
          </div>
          <div
            class="cards-wrapper row align-items-start justify-content-center justify-content-sm-start justify-content-md-evenly">
            <!-- ecah card -->
            <div class="col-md-3 p-0 each-card" data-aos="fade-right" data-aos-delay="200">
              <div class="each-card-inner">
                <div class="card-title">
                  <h4>Basic</h4>
                </div>
                <div class="price">
                  <h3>$ 10.00</h3>
                  <span>Per Month</span>
                </div>
                <div class="CAT">
                  <button>Choose Plan</button>
                </div>
                <ul>
                  <li>
                    <div class="badge-icon">
                      <em class="bi bi-patch-check-fill"></em>
                    </div>
                    <div class="text">
                      <span> Receive 100 Subscribers and followers across social mediums </span>
                    </div>
                  </li>
                  <li>
                    <div class="badge-icon">
                      <em class="bi bi-patch-check-fill"></em>
                    </div>
                    <div class="text">
                      <span> Receive 500 youtube watch seconds </span>
                    </div>
                  </li>
                  <li>
                    <div class="badge-icon">
                      <em class="bi bi-patch-check-fill"></em>
                    </div>
                    <div class="text">
                      <span> Receive 500 visit on your blogs links </span>
                    </div>
                  </li>
                  <li>
                    <div class="badge-icon">
                      <em class="bi bi-patch-check-fill"></em>
                    </div>
                    <div class="text">
                      <span> Receive 100 Reactions across Social Mediums</span>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
            <!-- each card end -->
            <!-- ecah card -->
            <div class="col-md-3 p-0 each-card" data-aos="fade-right" data-aos-delay="500">
              <div class="each-card-inner">
                <div class="card-title">
                  <h4>Premium</h4>
                </div>
                <div class="price">
                  <h3>$ 20.00</h3>
                  <span>Per Month</span>
                </div>
                <div class="CAT">
                  <button>Choose Plan</button>
                </div>
                <ul>
                  <li>
                    <div class="badge-icon">
                      <em class="bi bi-patch-check-fill"></em>
                    </div>
                    <div class="text">
                      <span> Receive 500 Subscribers and followers across social mediums </span>
                    </div>
                  </li>
                  <li>
                    <div class="badge-icon">
                      <em class="bi bi-patch-check-fill"></em>
                    </div>
                    <div class="text">
                      <span> Receive 2500 youtube watch seconds </span>
                    </div>
                  </li>
                  <li>
                    <div class="badge-icon">
                      <em class="bi bi-patch-check-fill"></em>
                    </div>
                    <div class="text">
                      <span> Receive 2500 visit on your blogs links </span>
                    </div>
                  </li>
                  <li>
                    <div class="badge-icon">
                      <em class="bi bi-patch-check-fill"></em>
                    </div>
                    <div class="text">
                      <span> Receive 500 Reactions across Social Mediums</span>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
            <!-- each card end -->
            <!-- ecah card -->
            <div class="col-md-3 p-0 each-card" data-aos="fade-right" data-aos-delay="800">
              <div class="each-card-inner">
                <div class="card-title">
                  <h4>Affiliate</h4>
                </div>
                <div class="price">
                  <h3>$ 40.00</h3>
                  <span>Per Month</span>
                </div>
                <div class="CAT">
                  <button>Choose Plan</button>
                </div>
                <ul>
                  <li>
                    <div class="badge-icon"><em class="bi bi-patch-check-fill"></em></div>
                    <div class="text">
                      <span> Receive 1000 Subscribers and followers across social mediums </span>
                    </div>
                  </li>
                  <li>
                    <div class="badge-icon"><em class="bi bi-patch-check-fill"></em></div>
                    <div class="text">
                      <span> Receive 5000 youtube watch seconds</span>
                    </div>
                  </li>
                  <li>
                    <div class="badge-icon"><em class="bi bi-patch-check-fill"></em></div>
                    <div class="text">
                      <span> Receive 5000 visit on your blogs links</span>
                    </div>
                  </li>
                  <li>
                    <div class="badge-icon"><em class="bi bi-patch-check-fill"></em></div>
                    <div class="text">
                      <span> Receive 10000 Reactions across Social Mediums Multilevel Referral Bonus plan</span>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
            <!-- each card end -->
          </div>
        </section>
        <!-- section five ends -->
      </div>
      <!-- section eight -->
    </div>
    <section class="eight">
      <FAQ></FAQ>
    </section>
  </div>
</template>

<script>
import FAQ from '@/components/FaqMain.vue'

export default {
  name: 'App',
  components: {
    FAQ,
  }

}
</script>