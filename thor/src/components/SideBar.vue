<template>
  <div class="nav-sidebar p-0 d-none d-md-inline-flex col-md-3">
    <div class="nav-sidebar-inner">
      <div class="nav-sidebar-logo">
        <router-link to="/"><img src="../assets/static/images/variant-logo.svg" alt="" class="img-fluid" /></router-link>
      </div>
      <div class="nav-sidebar-content">
        <ul class="nav-links">
          <li class="each-nav-link">
            <router-link to="/dashboard" class="nav-link-item">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  preserveAspectRatio="xMidYMid meet"
                  viewBox="0 0 24 24">
                  <path
                    fill="none"
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M3 3h7v9H3zm11 0h7v5h-7zm0 9h7v9h-7zM3 16h7v5H3z" />
                </svg>
              </span>
              <span>Dashboard</span>
            </router-link>
          </li>
          <li class="each-nav-link">
            <router-link to="/blog" class="nav-link-item">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  preserveAspectRatio="xMidYMid meet"
                  viewBox="0 0 24 24">
                  <path
                    fill="currentColor"
                    d="M20 22H4a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1zm-1-2V4H5v16h14zM8 7h8v2H8V7zm0 4h8v2H8v-2zm0 4h5v2H8v-2z" />
                </svg>
              </span>
              <span>Post</span>
            </router-link>
          </li>
          <li class="each-nav-link">
            <router-link to="/contents" class="nav-link-item">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  preserveAspectRatio="xMidYMid meet"
                  viewBox="0 0 48 48">
                  <g transform="translate(48 0) scale(-1 1)">
                    <g
                      fill="none"
                      stroke="currentColor"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="4">
                      <path
                        d="M26.2401 16.373L17.1001 7.23303C14.4388 4.57168 10.0653 4.6303 7.33158 7.36397C4.59791 10.0976 4.53929 14.4712 7.20064 17.1325L15.1359 25.0678" />
                      <path
                        d="M32.9027 23.0031L40.838 30.9384C43.4994 33.5998 43.4407 37.9733 40.7071 40.707C37.9734 43.4407 33.5999 43.4993 30.9385 40.8379L21.7985 31.6979" />
                      <path d="M26.1093 26.1416C28.843 23.4079 28.9016 19.0344 26.2403 16.373" />
                      <path d="M21.7989 21.7984C19.0652 24.5321 19.0066 28.9056 21.6679 31.5669" />
                    </g>
                  </g>
                </svg>
              </span>
              <span>Link</span>
            </router-link>
          </li>
          <li class="each-nav-link">
            <router-link to="/schedule" class="nav-link-item">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  preserveAspectRatio="xMidYMid meet"
                  viewBox="0 0 16 16">
                  <g transform="translate(16 0) scale(-1 1)">
                    <g fill="currentColor">
                      <path
                        d="M4.5 6a.5.5 0 1 0 0-1a.5.5 0 0 0 0 1ZM6 6a.5.5 0 1 0 0-1a.5.5 0 0 0 0 1Zm2-.5a.5.5 0 1 1-1 0a.5.5 0 0 1 1 0Z" />
                      <path
                        d="M12 1a2 2 0 0 1 2 2a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h10ZM2 12V5a2 2 0 0 1 2-2h9a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1Zm1-4v5a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V8H3Zm12-1V5a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v2h12Z" />
                    </g>
                  </g>
                </svg>
              </span>
              <span>Schedule</span>
            </router-link>
          </li>
          <li class="each-nav-link">
            <router-link to="/settings" class="nav-link-item">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  preserveAspectRatio="xMidYMid meet"
                  viewBox="0 0 36 36">
                  <g transform="translate(36 0) scale(-1 1)">
                    <path
                      fill="currentColor"
                      d="M18.1 11c-3.9 0-7 3.1-7 7s3.1 7 7 7s7-3.1 7-7s-3.1-7-7-7zm0 12c-2.8 0-5-2.2-5-5s2.2-5 5-5s5 2.2 5 5s-2.2 5-5 5z"
                      class="clr-i-outline clr-i-outline-path-1" />
                    <path
                      fill="currentColor"
                      d="m32.8 14.7l-2.8-.9l-.6-1.5l1.4-2.6c.3-.6.2-1.4-.3-1.9l-2.4-2.4c-.5-.5-1.3-.6-1.9-.3l-2.6 1.4l-1.5-.6l-.9-2.8C21 2.5 20.4 2 19.7 2h-3.4c-.7 0-1.3.5-1.4 1.2L14 6c-.6.1-1.1.3-1.6.6L9.8 5.2c-.6-.3-1.4-.2-1.9.3L5.5 7.9c-.5.5-.6 1.3-.3 1.9l1.3 2.5c-.2.5-.4 1.1-.6 1.6l-2.8.9c-.6.2-1.1.8-1.1 1.5v3.4c0 .7.5 1.3 1.2 1.5l2.8.9l.6 1.5l-1.4 2.6c-.3.6-.2 1.4.3 1.9l2.4 2.4c.5.5 1.3.6 1.9.3l2.6-1.4l1.5.6l.9 2.9c.2.6.8 1.1 1.5 1.1h3.4c.7 0 1.3-.5 1.5-1.1l.9-2.9l1.5-.6l2.6 1.4c.6.3 1.4.2 1.9-.3l2.4-2.4c.5-.5.6-1.3.3-1.9l-1.4-2.6l.6-1.5l2.9-.9c.6-.2 1.1-.8 1.1-1.5v-3.4c0-.7-.5-1.4-1.2-1.6zm-.8 4.7l-3.6 1.1l-.1.5l-.9 2.1l-.3.5l1.8 3.3l-2 2l-3.3-1.8l-.5.3c-.7.4-1.4.7-2.1.9l-.5.1l-1.1 3.6h-2.8l-1.1-3.6l-.5-.1l-2.1-.9l-.5-.3l-3.3 1.8l-2-2l1.8-3.3l-.3-.5c-.4-.7-.7-1.4-.9-2.1l-.1-.5L4 19.4v-2.8l3.4-1l.2-.5c.2-.8.5-1.5.9-2.2l.3-.5l-1.7-3.3l2-2l3.2 1.8l.5-.3c.7-.4 1.4-.7 2.2-.9l.5-.2L16.6 4h2.8l1.1 3.5l.5.2c.7.2 1.4.5 2.1.9l.5.3l3.3-1.8l2 2l-1.8 3.3l.3.5c.4.7.7 1.4.9 2.1l.1.5l3.6 1.1v2.8z"
                      class="clr-i-outline clr-i-outline-path-2" />
                    <path fill="none" d="M0 0h36v36H0z" />
                  </g>
                </svg>
              </span>
              <span>Settings</span>
            </router-link>
          </li>
        </ul>
        <ul class="nav-links">
          <li class="each-nav-link">
            <router-link to="/logout" class="nav-link-item">
              <span>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="32"
                  height="32"
                  preserveAspectRatio="xMidYMid meet"
                  viewBox="0 0 24 24">
                  <g transform="rotate(180 12 12)">
                    <path
                      fill="currentColor"
                      d="M6 2h9a2 2 0 0 1 2 2v1a1 1 0 0 1-2 0V4H6v16h9v-1a1 1 0 0 1 2 0v1a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z" />
                    <path
                      fill="currentColor"
                      d="M16.795 16.295c.39.39 1.02.39 1.41 0l3.588-3.588a1 1 0 0 0 0-1.414l-3.588-3.588a.999.999 0 0 0-1.411 1.411L18.67 11H10a1 1 0 0 0 0 2h8.67l-1.876 1.884a.999.999 0 0 0 .001 1.411z" />
                  </g>
                </svg>
              </span>
              <span>Log out</span>
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script setup>
</script>