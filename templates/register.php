<?php
session_start();

if(!isset($_SESSION['user_email'])){
  
  if(isset($_POST['submit'])){
    $dbc = mysqli_connect('ec2-52-53-189-246.us-west-1.compute.amazonaws.com','user','12345678','cc');
    $user_email = mysqli_real_escape_string($dbc,trim($_POST['email']));
    $user_password = mysqli_real_escape_string($dbc,trim($_POST['password']));
  
    if(!empty($user_email)){
      $query = "SELECT email FROM user WHERE  email = '$user_email'";
      $data = mysqli_query($dbc,$query);
      
      if(mysqli_num_rows($data)==1){
        echo "<script>alert('$user_email has been registered'); history.go(-1);</script>";
      }
      else{
        if(!empty($user_password))
        {
          $query_reg = "INSERT INTO user VALUES('$user_email','$user_password')";
          mysqli_query($dbc,$query_reg);

          $home_url = 'index.html';
          header('Location: '.$home_url);
        }
        else
          echo 'Sorry, you must enter a valid password to log in.';
      }
    
    }
    
    else{
      echo 'Sorry, you must enter a valid email to log in.';
    }

}  

}

else{
  $home_url = 'loged.php';
  header('Location: '.$home_url);
}
?>