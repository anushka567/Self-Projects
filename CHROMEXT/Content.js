const generateHTML=(pagename)=>{
  return `
 <meta name="google" content="notranslate">
  <div class='c'>
  <div><h1>Study Don't Waste Time</h1></div>
  <div class="bottom">NO ${pagename}</div>
  </div>
  <br><br>
  
  
  `;
}

const generateSTYLING=()=>{
    return`
    <style>
    *{
        padding:0
        margin:0
    }
    body{
        background-color:#59981A
    }
    .c{
        margin-top:20vh
    }
    img{
      left:30vw
    }
    .bottom,h1,.gru{
           text-align:center;
    }
    #goog-gt-tt{
        opacity:0
    }

    </style>
    `;
}

switch (window.location.hostname )
{
   case "www.youtube.com":
          document.head.innerHTML=generateSTYLING();
          document.body.innerHTML=generateHTML("YOUTUBE");
         break;
    case "www.facebook.com":
          document.head.innerHTML=generateSTYLING();
          document.body.innerHTML=generateHTML("FACEBOOK");
         break;
    case "www.twitter.com":
          document.head.innerHTML=generateSTYLING();
          document.body.innerHTML=generateHTML("TWITTER");
         break;
    case "www.reddit.com":
         document.head.innerHTML=generateSTYLING();
          document.body.innerHTML=generateHTML("REDDIT");
         break;
    case "www.instagram.com":
          document.head.innerHTML=generateSTYLING();
          document.body.innerHTML=generateHTML("INSTAGRAM");
         break;
   
}
