-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 18, 2022 at 08:05 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(60) NOT NULL,
  `phone_num` varchar(15) NOT NULL,
  `mes` text NOT NULL,
  `date` datetime(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `mes`, `date`) VALUES
(1, '', '', '', 'this is a test message', '2022-08-13 19:24:22.000000'),
(39, 'harry', 'ceknigatra@vusra.com', '99999999999', 'this is harry, thank you!', '2022-08-14 21:45:59.942902');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `author` text NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(100) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `slug`, `title`, `tagline`, `author`, `content`, `img_file`, `date`) VALUES
(1, 'About-Cryptography_harry-ari', 'About Cryptography By Harry & Ari', 'Study of data security through Encryption technique', 'Harry_Arijit', 'Cryptography is the study of data security through Encryption technique, which describe the encryption process and techniques used.\r\n\r\nA cipher is an algorithm which is used to encrypt or decrypt the data. Plain text is converted in cipher text with help of this. The transforming process is performed using a key.\r\n\r\nThis key is like a pattern to encrypt the data. If we wanted to decrypt the data then we need to reverse the process.\r\n- Thanking you (Harry & Ari)', 'cryptography.jfif', '2022-08-16'),
(2, 'Back-End-Web-Architecture', 'Back-End Web Architecture', 'Overview of servers, databases, routing', 'Codecademy Team', 'Software engineers seem to always be discussing the front-end and the back-end of their apps. But what exactly does this mean?\r\n\r\nThe front-end is the code that is executed on the client side. This code (typically HTML, CSS, and JavaScript) runs in the user’s browser and creates the user interface.\r\n\r\nThe back-end is the code that runs on the server, that receives requests from the clients, and contains the logic to send the appropriate data back to the client. The back-end also includes the database, which will persistently store all of the data for the application. This article focuses on the hardware and software on the server-side that make this possible.\r\n\r\nReview HTTP and REST if you want to refresh your memory on these topics. These are the main conventions that provide structure to the request-response cycle between clients and servers.\r\n\r\nLet’s start by reviewing the client-server relationship, and then we can start to put the pieces all together!', 'Back-End Web Architecture.png', '2022-08-17'),
(3, 'Build-a-3D-Environment-with-Three.js', '#new Build a 3D Environment', 'Build a 3D environment with Three.js', 'Harry & Arijit', 'It should be noted that the Three.js API uses a considerable amount of stage and camera projection terms to name classes, functions and parameters.\r\n\r\nThe renderer object is the root of a Three.js program and carries two parameters:\r\n\r\nA Scene object that contains 3D objects, lights, cameras, etc.\r\nA Camera, which is an object-based abstraction of a camera view that exists both inside and outside of scenes.\r\nScenes and their child elements make up the scenegraph, a tree-like representation of the parent/child-relationship between objects in the scene. Scenegraphs can also contain zero or more cameras.\r\n\r\nCameras use methods that utilize parameters named after terms in camera projection. The following terms define the observable “shape” (or frustum) of the camera:\r\n\r\nfov stands for field of view, which is the range of the observable world from a (camera’s) perspective at a given moment in time, measured in degrees.\r\naspect describes the width:height ratio of the to-be-rendered <canvas> element.\r\nnear and far define the range of viewable space between the camera lens and the drawn objects.\r\nWith some terms out of the way, let’s begin building a 3D environment.', 'Build a 3D Environment with Three js.jpg', '2022-08-16'),
(4, '“learn-to-code”-movement', 'Learn To Code Movement', 'Learn To Code', 'Ivan Ruby', 'In an era of an insecure job market, when redundant professions are projected to be eliminated while new ones arise, learning to code gives hope to our collective imagination. It creates the promise of alternative sources of income as well as opportunities for self-employment given the demand of coding skills in a variety of industries.\r\n\r\nLearning to code is not just a younger-generation trend. For example, Scratch is a popular tool used in and outside of classrooms to create, share and remix games. It allows intergenerational learning where youth, adults and seniors can create game prototypes.\r\n\r\nCoding can be used to automate tasks, solve complex problems, forecast, or simulate events that did not happen yet. A trendy area of interest for businesses is data analytics, a field involving making sense of massive amounts of data.', 'learn to code.jfif', '2022-08-14'),
(5, 'AWS-Account-Setup', 'AWS Account Setup', 'Get started with AWS', 'Codecademy Team', 'In this article, we will explain how to sign up for an AWS free tier account and walk through the following:\r\n\r\nUsing the AWS console to sign up for an account\r\nAn overview of services in a free account\r\nBilling\r\nMulti-Factor Authentication (MFA)\r\nThe AWS pricing model\r\nLaunching a free EC2 instance\r\nA fear many people have about using AWS is the cost. But there is good news. With careful use, AWS can be completely free. Even with the paid features, if you use only a small amount of its resources, it can cost as little as a few dollars a month. We will dive deeper into the different plans and pricing later on in this article.\r\n\r\nLet’s get started by first creating a free account.', 'Get started with AWS.png', '2022-08-14'),
(6, 'Accessibility-and-HTML', 'Accessibility and HTML', 'Content accessible to visually-impaired users', 'CodeCademy Team', 'When designing and creating web pages, it’s important that the web pages are accessible to all audiences. In particular, due to the visual and dynamic nature of the webpages that you’ll be making, it’s important to make sure that your website will also make sense to visually-impaired or blind users.\r\n\r\nMany visually-impaired or blind users access web pages with the help of screen readers. Screen readers parse through the HTML of your web page and read the contents out loud, responding to commands to navigate around the page, and take actions such as clicking on a link, typing in an input field, or submitting a form. In this resource, we’ll give an overview of a few ways that you can improve the accessibility of your web page and help screen readers better interpret it!', 'Accessibility and HTML.jpg', '2022-08-14'),
(15, 'IntroductiontoDjango', 'Puja Dhamaka Offer', '7 tagline', 'raj', 'afwqesdfsweqrwefsd', 'fsd', '2022-08-17');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
