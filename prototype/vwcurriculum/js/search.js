function searchCertificate() {
  var input, filter, ul, li, span, i;
  input = document.getElementById('searchCertificateInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("searchCertificateUL");
  li = ul.getElementsByTagName('li');

  for (i = 0; i < li.length; i++) {
    span = li[i].getElementsByTagName("span")[0];
    if (span.innerHTML.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
function searchProject() {
  var input, filter, ul, li, span, i;
  input = document.getElementById('searchProjectInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("searchProjectUL");
  li = ul.getElementsByTagName('li');

  for (i = 0; i < li.length; i++) {
    span = li[i].getElementsByTagName("span")[0];
    if (span.innerHTML.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
function searchExperience() {
  var input, filter, ul, li, span, i;
  input = document.getElementById('searchExperienceInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("searchExperienceUL");
  li = ul.getElementsByTagName('li');

  for (i = 0; i < li.length; i++) {
    span = li[i].getElementsByTagName("span")[0];
    if (span.innerHTML.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
