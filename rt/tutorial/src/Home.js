import { block } from 'strip-comments';

function Home(){
    return (

    
      <div className="content">
      <div id="home" style={{display: block,}}>
          <div className="bg"></div>
          <div className="bg bg2"></div>
          <div className="bg bg3"></div>
          <main role="main" class="container ">
              <svg viewBox="0 0 461 295" fill="none" xmlns="http://www.w3.org/2000/svg" id="lg-logo">
                  <path d="M59.744 79.368C59.744 75.336 58.544 72.072 56.144 69.576C53.744 66.984 50.72 64.728 47.072 62.808C43.52 60.792 39.632 58.92 35.408 57.192C31.184 55.464 27.248 53.4 23.6 51C20.048 48.504 17.072 45.48 14.672 41.928C12.272 38.28 11.072 33.672 11.072 28.104C11.072 20.232 13.808 13.992 19.28 9.38398C24.752 4.77598 32.528 2.47198 42.608 2.47198C48.464 2.47198 53.792 2.90398 58.592 3.76798C63.392 4.63198 67.136 5.73598 69.824 7.07998L66.224 17.592C64.016 16.536 60.752 15.528 56.432 14.568C52.208 13.608 47.408 13.128 42.032 13.128C35.696 13.128 30.944 14.568 27.776 17.448C24.608 20.232 23.024 23.544 23.024 27.384C23.024 31.128 24.224 34.248 26.624 36.744C29.024 39.24 32 41.496 35.552 43.512C39.2 45.432 43.136 47.352 47.36 49.272C51.584 51.192 55.472 53.448 59.024 56.04C62.672 58.536 65.696 61.56 68.096 65.112C70.496 68.664 71.696 73.08 71.696 78.36C71.696 82.68 70.928 86.568 69.392 90.024C67.856 93.48 65.6 96.456 62.624 98.952C59.648 101.448 56.048 103.368 51.824 104.712C47.6 106.056 42.8 106.728 37.424 106.728C30.224 106.728 24.272 106.152 19.568 105C14.864 103.944 11.216 102.744 8.62398 101.4L12.656 90.6C14.864 91.848 18.128 93.096 22.448 94.344C26.768 95.496 31.616 96.072 36.992 96.072C40.16 96.072 43.136 95.784 45.92 95.208C48.704 94.536 51.104 93.528 53.12 92.184C55.136 90.744 56.72 88.968 57.872 86.856C59.12 84.744 59.744 82.248 59.744 79.368Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
                  <path d="M88.436 38.328C92.084 36.12 96.308 34.488 101.108 33.432C106.004 32.376 111.092 31.848 116.372 31.848C121.364 31.848 125.348 32.52 128.324 33.864C131.396 35.208 133.7 36.984 135.236 39.192C136.868 41.304 137.924 43.656 138.404 46.248C138.98 48.84 139.268 51.432 139.268 54.024C139.268 59.784 139.124 65.4 138.836 70.872C138.548 76.344 138.404 81.528 138.404 86.424C138.404 89.976 138.548 93.336 138.836 96.504C139.124 99.672 139.652 102.6 140.42 105.288H131.924L128.9 95.208H128.18C127.316 96.552 126.212 97.896 124.868 99.24C123.62 100.488 122.084 101.64 120.26 102.696C118.436 103.656 116.324 104.472 113.924 105.144C111.524 105.816 108.788 106.152 105.716 106.152C102.644 106.152 99.764 105.672 97.076 104.712C94.484 103.752 92.228 102.408 90.308 100.68C88.388 98.856 86.852 96.696 85.7 94.2C84.644 91.704 84.116 88.872 84.116 85.704C84.116 81.48 84.98 77.976 86.708 75.192C88.436 72.312 90.836 70.056 93.908 68.424C97.076 66.696 100.82 65.496 105.14 64.824C109.556 64.056 114.404 63.672 119.684 63.672C121.028 63.672 122.324 63.672 123.572 63.672C124.916 63.672 126.26 63.768 127.604 63.96C127.892 61.08 128.036 58.488 128.036 56.184C128.036 50.904 126.98 47.208 124.868 45.096C122.756 42.984 118.916 41.928 113.348 41.928C111.716 41.928 109.94 42.072 108.02 42.36C106.196 42.552 104.276 42.888 102.26 43.368C100.34 43.752 98.468 44.28 96.644 44.952C94.916 45.528 93.38 46.2 92.036 46.968L88.436 38.328ZM108.884 96.072C111.572 96.072 113.972 95.736 116.084 95.064C118.196 94.296 120.02 93.384 121.556 92.328C123.092 91.176 124.34 89.928 125.3 88.584C126.356 87.24 127.124 85.944 127.604 84.696V72.744C126.26 72.648 124.868 72.6 123.428 72.6C122.084 72.504 120.74 72.456 119.396 72.456C116.42 72.456 113.492 72.648 110.612 73.032C107.828 73.32 105.332 73.944 103.124 74.904C101.012 75.768 99.284 77.016 97.94 78.648C96.692 80.184 96.068 82.152 96.068 84.552C96.068 87.912 97.268 90.696 99.668 92.904C102.068 95.016 105.14 96.072 108.884 96.072Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
                  <path d="M203.217 105V64.248C203.217 60.408 203.025 57.096 202.641 54.312C202.353 51.432 201.729 49.032 200.769 47.112C199.809 45.192 198.417 43.752 196.593 42.792C194.865 41.832 192.561 41.352 189.681 41.352C185.265 41.352 181.569 42.696 178.593 45.384C175.713 48.072 173.697 51.432 172.545 55.464V105H161.025V33H169.089L171.249 41.784H171.825C174.417 38.712 177.393 36.216 180.753 34.296C184.209 32.28 188.673 31.272 194.145 31.272C198.753 31.272 202.497 32.184 205.377 34.008C208.353 35.736 210.657 38.808 212.289 43.224C214.497 39.48 217.521 36.552 221.361 34.44C225.297 32.328 229.713 31.272 234.609 31.272C238.641 31.272 242.049 31.752 244.833 32.712C247.617 33.576 249.921 35.16 251.745 37.464C253.569 39.768 254.865 42.888 255.633 46.824C256.497 50.76 256.929 55.752 256.929 61.8V105H245.409V61.656C245.409 58.2 245.217 55.224 244.833 52.728C244.545 50.136 243.873 48.024 242.817 46.392C241.857 44.664 240.465 43.416 238.641 42.648C236.913 41.784 234.609 41.352 231.729 41.352C226.929 41.352 223.185 42.696 220.497 45.384C217.809 48.072 215.889 51.912 214.737 56.904V105H203.217Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
                  <path d="M288.253 33V74.04C288.253 77.784 288.445 81.096 288.829 83.976C289.309 86.76 290.077 89.112 291.133 91.032C292.189 92.856 293.629 94.248 295.453 95.208C297.277 96.168 299.581 96.648 302.365 96.648C304.957 96.648 307.261 96.264 309.277 95.496C311.293 94.632 313.069 93.48 314.605 92.04C316.237 90.6 317.629 88.968 318.781 87.144C320.029 85.224 321.037 83.208 321.805 81.096V33H333.325V84.552C333.325 88.008 333.421 91.608 333.613 95.352C333.901 99 334.333 102.216 334.909 105H326.989L324.109 93.624H323.389C321.181 97.368 318.205 100.488 314.461 102.984C310.717 105.48 305.965 106.728 300.205 106.728C296.365 106.728 292.957 106.248 289.981 105.288C287.101 104.424 284.653 102.84 282.637 100.536C280.717 98.232 279.229 95.16 278.173 91.32C277.213 87.384 276.733 82.44 276.733 76.488V33H288.253Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
                  <path d="M408.07 99.24C405.19 101.544 401.542 103.368 397.126 104.712C392.806 106.056 388.198 106.728 383.302 106.728C377.83 106.728 373.078 105.864 369.046 104.136C365.014 102.312 361.702 99.768 359.11 96.504C356.518 93.144 354.598 89.16 353.35 84.552C352.102 79.944 351.478 74.76 351.478 69C351.478 56.712 354.214 47.352 359.686 40.92C365.158 34.488 372.982 31.272 383.158 31.272C386.422 31.272 389.686 31.656 392.95 32.424C396.214 33.096 399.142 34.44 401.734 36.456C404.326 38.472 406.438 41.352 408.07 45.096C409.702 48.744 410.518 53.592 410.518 59.64C410.518 62.808 410.23 66.312 409.654 70.152H363.43C363.43 74.376 363.862 78.12 364.726 81.384C365.59 84.648 366.934 87.432 368.758 89.736C370.582 91.944 372.934 93.672 375.814 94.92C378.79 96.072 382.39 96.648 386.614 96.648C389.878 96.648 393.142 96.072 396.406 94.92C399.67 93.768 402.118 92.424 403.75 90.888L408.07 99.24ZM383.302 41.352C377.638 41.352 373.078 42.84 369.622 45.816C366.262 48.792 364.246 53.88 363.574 61.08H399.286C399.286 53.784 397.894 48.696 395.11 45.816C392.326 42.84 388.39 41.352 383.302 41.352Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
                  <path d="M441.451 87.288C441.451 90.648 442.027 93.048 443.179 94.488C444.331 95.928 445.963 96.648 448.075 96.648C449.323 96.648 450.667 96.552 452.107 96.36C453.547 96.168 455.179 95.736 457.003 95.064L458.299 104.136C456.763 104.904 454.603 105.528 451.819 106.008C449.131 106.488 446.779 106.728 444.763 106.728C440.443 106.728 436.891 105.528 434.107 103.128C431.323 100.632 429.931 96.456 429.931 90.6V4.19998H441.451V87.288Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
                  <path d="M33.968 257.736L36.272 274.44H36.416L38.864 257.448L59.6 190.2H65.36L86.24 257.736L88.688 274.44H88.832L91.424 257.448L108.416 190.2H120.08L92 292.584H85.376L64.928 225.048L62.336 209.784H61.616L59.024 225.192L38.576 292.584H31.952L3.15198 190.2H15.824L33.968 257.736Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
                  <path d="M125.28 224.328C128.928 222.12 133.152 220.488 137.952 219.432C142.848 218.376 147.936 217.848 153.216 217.848C158.208 217.848 162.192 218.52 165.168 219.864C168.24 221.208 170.544 222.984 172.08 225.192C173.712 227.304 174.768 229.656 175.248 232.248C175.824 234.84 176.112 237.432 176.112 240.024C176.112 245.784 175.968 251.4 175.68 256.872C175.392 262.344 175.248 267.528 175.248 272.424C175.248 275.976 175.392 279.336 175.68 282.504C175.968 285.672 176.496 288.6 177.264 291.288H168.768L165.744 281.208H165.024C164.16 282.552 163.056 283.896 161.712 285.24C160.464 286.488 158.928 287.64 157.104 288.696C155.28 289.656 153.168 290.472 150.768 291.144C148.368 291.816 145.632 292.152 142.56 292.152C139.488 292.152 136.608 291.672 133.92 290.712C131.328 289.752 129.072 288.408 127.152 286.68C125.232 284.856 123.696 282.696 122.544 280.2C121.488 277.704 120.96 274.872 120.96 271.704C120.96 267.48 121.824 263.976 123.552 261.192C125.28 258.312 127.68 256.056 130.752 254.424C133.92 252.696 137.664 251.496 141.984 250.824C146.4 250.056 151.248 249.672 156.528 249.672C157.872 249.672 159.168 249.672 160.416 249.672C161.76 249.672 163.104 249.768 164.448 249.96C164.736 247.08 164.88 244.488 164.88 242.184C164.88 236.904 163.824 233.208 161.712 231.096C159.6 228.984 155.76 227.928 150.192 227.928C148.56 227.928 146.784 228.072 144.864 228.36C143.04 228.552 141.12 228.888 139.104 229.368C137.184 229.752 135.312 230.28 133.488 230.952C131.76 231.528 130.224 232.2 128.88 232.968L125.28 224.328ZM145.728 282.072C148.416 282.072 150.816 281.736 152.928 281.064C155.04 280.296 156.864 279.384 158.4 278.328C159.936 277.176 161.184 275.928 162.144 274.584C163.2 273.24 163.968 271.944 164.448 270.696V258.744C163.104 258.648 161.712 258.6 160.272 258.6C158.928 258.504 157.584 258.456 156.24 258.456C153.264 258.456 150.336 258.648 147.456 259.032C144.672 259.32 142.176 259.944 139.968 260.904C137.856 261.768 136.128 263.016 134.784 264.648C133.536 266.184 132.912 268.152 132.912 270.552C132.912 273.912 134.112 276.696 136.512 278.904C138.912 281.016 141.984 282.072 145.728 282.072Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
                  <path d="M229.549 271.416C229.549 268.536 228.685 266.28 226.957 264.648C225.229 263.016 223.069 261.672 220.477 260.616C217.981 259.464 215.197 258.408 212.125 257.448C209.149 256.392 206.365 255.096 203.773 253.56C201.277 251.928 199.165 249.864 197.437 247.368C195.709 244.872 194.845 241.512 194.845 237.288C194.845 230.376 196.813 225.336 200.749 222.168C204.685 218.904 210.157 217.272 217.165 217.272C222.349 217.272 226.669 217.752 230.125 218.712C233.677 219.576 236.749 220.632 239.341 221.88L236.605 231.384C234.397 230.328 231.709 229.416 228.541 228.648C225.469 227.784 222.157 227.352 218.605 227.352C214.381 227.352 211.261 228.072 209.245 229.512C207.325 230.952 206.365 233.448 206.365 237C206.365 239.496 207.229 241.464 208.957 242.904C210.685 244.248 212.797 245.496 215.293 246.648C217.885 247.704 220.669 248.76 223.645 249.816C226.717 250.872 229.501 252.264 231.997 253.992C234.589 255.72 236.749 257.928 238.477 260.616C240.205 263.208 241.069 266.664 241.069 270.984C241.069 274.056 240.541 276.936 239.485 279.624C238.525 282.312 236.989 284.616 234.877 286.536C232.765 288.456 230.125 289.944 226.957 291C223.885 292.152 220.237 292.728 216.013 292.728C210.541 292.728 205.885 292.2 202.045 291.144C198.205 290.088 194.989 288.84 192.397 287.4L195.853 277.608C198.061 278.856 200.941 280.008 204.493 281.064C208.045 282.12 211.645 282.648 215.293 282.648C219.421 282.648 222.829 281.832 225.517 280.2C228.205 278.568 229.549 275.64 229.549 271.416Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
                  <path d="M304.703 291V249.96C304.703 246.216 304.463 242.952 303.983 240.168C303.599 237.288 302.831 234.936 301.679 233.112C300.527 231.192 298.943 229.752 296.927 228.792C295.007 227.832 292.463 227.352 289.295 227.352C284.783 227.352 280.703 228.84 277.055 231.816C273.407 234.696 271.055 238.44 269.999 243.048V291H258.479V190.2H269.999V227.064H270.575C273.071 224.088 276.047 221.736 279.503 220.008C283.055 218.184 287.423 217.272 292.607 217.272C296.639 217.272 300.143 217.752 303.119 218.712C306.095 219.576 308.543 221.16 310.463 223.464C312.479 225.768 313.919 228.888 314.783 232.824C315.743 236.664 316.223 241.56 316.223 247.512V291H304.703Z" stroke="#C5C6C7" stroke-width="4" mask="url(#path-1-outside-1)"></path>
              </svg>
              <span id="sm-logo"> S <br/> G <br/>W </span>
          </main>
        </div>
      </div>
    )
}

export default Home;