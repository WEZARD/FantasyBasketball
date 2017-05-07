<?php
session_start();

if(!isset($_SESSION['user_email'])){
  
  if(isset($_POST['submit'])){
    $dbc = mysqli_connect('ec2-52-53-189-246.us-west-1.compute.amazonaws.com','user','12345678','cc');
    $user_email = mysqli_real_escape_string($dbc,trim($_POST['email']));
    $user_password = mysqli_real_escape_string($dbc,trim($_POST['password']));
  
    
    if(!empty($user_email)){
      
      if(empty($user_password))
        echo "<script>alert('Please enter your password!'); history.go(－1);</script>";

      $query = "SELECT email FROM user WHERE  email = '$user_email'";
      $data = mysqli_query($dbc,$query);
      
      
      if(mysqli_num_rows($data)==1){
        $query_password = "SELECT password FROM user where email = '$user_email'";
        $var_password = mysqli_fetch_array(mysqli_query($dbc,$query_password));
        $db_password = $var_password['password'];
        if($user_password == $db_password)
        {
          $home_url = 'index.html';
          header('Location: '.$home_url);

        }
        else
        echo "<script>alert('Invalid email or password!'); history.go(-1);</script>";
        
      }
      else{
        echo "<script>alert('Invalid email or password!'); history.go(-1);</script>";
        }
       
    
    }
    
    else
      echo "<script>alert('Please enter an email!'); history.go(-1);</script>";


}  

}

?>