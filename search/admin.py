from django.contrib import admin
from .models import search

# Register your models here.

admin.site.register(search)



'''
Ahmedabad
Bangalore
Bhubaneswar
Chandigarh
Chennai
Delhi
Dewas
Ghaziabad
Hyderabad
Indore
Jaipur
Kolkata
Lucknow
Kanpur
Mumbai
Visakhapatnam
 '''
'''
  <form action="{%url 'searchpro'%}" method="post" class="contact-form-bottom">
{% csrf_token %}
<div class="error-container"></div>
<div class="row">
<input type="hidden" name="" value="">
<input type="hidden" name="" value="">
<input type="hidden" name="" value="">
<input type="hidden" name="" value="">




  <div >
    <div >
      <select name="select city" id="searchcity">
         <option value="select city">Select city</option>
         <option value="Ahmedabad">Ahmedabad</option>
         <option value="Bangalore">Bangalore</option>
         <option value="Bhubaneswar">Bhubaneswar</option>
         <option value="Chandigarh">Chandigarh</option>
         <option value="Chennai">Chennai</option>
         <option value="Delhi">Delhi</option>
         <option value="Dewas">Dewas</option>
         <option value="Ghaziabad">Ghaziabad</option>
         <option value="Hyderabad">Hyderabad</option>
         <option value="Indore">Indore</option>
         <option value="Jaipur">Jaipur</option>
         <option value="Kolkata">Kolkata</option>
         <option value="Lucknow">Lucknow</option>
         <option value="Kanpur">Kanpur</option>
         <option value="Mumbai">Mumbai</option>
         <option value="Visakhapatnam">Visakhapatnam</option>


      </select>
     </div>
   </div>
<div class="text-right"><br>
  <button class="btn btn-primary btn-full" type="submit"><i class="fa fa-paper-plane-o"></i> Send Message</button>
</div>
</form>
'''
