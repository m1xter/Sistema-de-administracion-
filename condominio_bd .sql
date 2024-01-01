-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 25, 2023 at 10:58 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `condominio_bd`
--

-- --------------------------------------------------------

--
-- Table structure for table `apartamentos`
--

CREATE TABLE `apartamentos` (
  `nro_aparta` int(2) NOT NULL COMMENT 'numero de apartamento',
  `Propietario` char(8) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `Inquilino` char(8) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_swedish_ci COMMENT='tabla de apartamentos';

--
-- Dumping data for table `apartamentos`
--

INSERT INTO `apartamentos` (`nro_aparta`, `Propietario`, `Inquilino`) VALUES
(20, '29976865', '6432135'),
(40, '29976865', '6432135');

-- --------------------------------------------------------

--
-- Table structure for table `egresos`
--

CREATE TABLE `egresos` (
  `id_egresos` int(11) NOT NULL COMMENT 'id del egreso',
  `fecha` date NOT NULL COMMENT 'fecha del egreso',
  `causa` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL COMMENT 'descripcion del egreso',
  `cant_retirada` int(10) UNSIGNED NOT NULL COMMENT 'cantidad del egreso'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ingresos`
--

CREATE TABLE `ingresos` (
  `id_ingreso` int(11) NOT NULL COMMENT 'id del pago',
  `nro_apartamento` int(11) NOT NULL COMMENT 'apartamento que hizo el pago',
  `fecha` date NOT NULL COMMENT 'fecha del realizacon del pago',
  `tipo_pago` varchar(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL COMMENT 'tipo de pago ralizado',
  `meses` varchar(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL COMMENT 'meses que se pagaron',
  `cant_dinero` int(11) NOT NULL COMMENT 'cantidad depositada'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='informacion de los pagos realizados';

-- --------------------------------------------------------

--
-- Table structure for table `mensualidad`
--

CREATE TABLE `mensualidad` (
  `apartamento` int(3) NOT NULL,
  `enero` varchar(2) NOT NULL,
  `febrero` varchar(2) NOT NULL,
  `marzo` varchar(2) NOT NULL,
  `abril` varchar(2) NOT NULL,
  `mayo` varchar(2) NOT NULL,
  `junio` varchar(2) NOT NULL,
  `julio` varchar(2) NOT NULL,
  `agosto` varchar(2) NOT NULL,
  `septiembre` varchar(2) NOT NULL,
  `octubre` varchar(2) NOT NULL,
  `noviembre` varchar(2) NOT NULL,
  `diciembre` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mensualidad`
--

INSERT INTO `mensualidad` (`apartamento`, `enero`, `febrero`, `marzo`, `abril`, `mayo`, `junio`, `julio`, `agosto`, `septiembre`, `octubre`, `noviembre`, `diciembre`) VALUES
(20, '', '', '', '', '', '', 'O', '', '', '', '', ''),
(40, '', '', '', '', '', '', 'O', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `personas`
--

CREATE TABLE `personas` (
  `cedula` char(8) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL COMMENT 'cedula de la persona',
  `primer_nombre` varchar(50) NOT NULL,
  `segundo_nombre` varchar(50) NOT NULL,
  `primer_apellido` varchar(50) NOT NULL,
  `segundo_apellido` varchar(50) NOT NULL,
  `nro_telefono` varchar(40) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `edad` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `personas`
--

INSERT INTO `personas` (`cedula`, `primer_nombre`, `segundo_nombre`, `primer_apellido`, `segundo_apellido`, `nro_telefono`, `tipo`, `edad`) VALUES
('29976865', 'juan', 'alejandro', 'Vizcaya', 'Gonzalez', '4161311419', 'propietario', '22'),
('30976865', 'juan', 'pedro', 'mora', 'gonzalez', '04161049951', 'inquilino', '22'),
('6432135', 'alejandro', 'daniel', 'gonzalo', 'vizcaya', '123554', 'inquilino', '50');

-- --------------------------------------------------------

--
-- Table structure for table `saldo_condo`
--

CREATE TABLE `saldo_condo` (
  `id_saldo` int(11) NOT NULL,
  `Saldo_condominio` float UNSIGNED NOT NULL COMMENT 'este es el salo del comdominio'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `saldo_condo`
--

INSERT INTO `saldo_condo` (`id_saldo`, `Saldo_condominio`) VALUES
(1, 23333);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(55) NOT NULL,
  `contrasena` varchar(55) NOT NULL,
  `permisos` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre_usuario`, `contrasena`, `permisos`) VALUES
(3, 'ale', '23', 'admin'),
(4, '', '', 'admin'),
(5, 'maria', '4567', 'admin'),
(6, 'juan', 'mostacho', 'normal'),
(7, 'pedro', '1234', 'Admin'),
(8, 'gonzalo', '4444', 'cliente'),
(9, 'alejandro', '34', 'cliente'),
(10, 'alejandro', '34', 'cliente'),
(11, 'wirzi_9', '13351834a', 'cliente'),
(12, 'alejandro', 'pe', 'tesorero');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `apartamentos`
--
ALTER TABLE `apartamentos`
  ADD PRIMARY KEY (`nro_aparta`),
  ADD KEY `id_propietario` (`Propietario`),
  ADD KEY `id_inquilino` (`Inquilino`);

--
-- Indexes for table `egresos`
--
ALTER TABLE `egresos`
  ADD PRIMARY KEY (`id_egresos`);

--
-- Indexes for table `ingresos`
--
ALTER TABLE `ingresos`
  ADD PRIMARY KEY (`id_ingreso`),
  ADD KEY `nro_aparta` (`nro_apartamento`);

--
-- Indexes for table `mensualidad`
--
ALTER TABLE `mensualidad`
  ADD PRIMARY KEY (`apartamento`);

--
-- Indexes for table `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`cedula`);

--
-- Indexes for table `saldo_condo`
--
ALTER TABLE `saldo_condo`
  ADD PRIMARY KEY (`id_saldo`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `egresos`
--
ALTER TABLE `egresos`
  MODIFY `id_egresos` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id del egreso', AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `ingresos`
--
ALTER TABLE `ingresos`
  MODIFY `id_ingreso` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id del pago', AUTO_INCREMENT=80;

--
-- AUTO_INCREMENT for table `saldo_condo`
--
ALTER TABLE `saldo_condo`
  MODIFY `id_saldo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `apartamentos`
--
ALTER TABLE `apartamentos`
  ADD CONSTRAINT `apartamentos_ibfk_1` FOREIGN KEY (`Propietario`) REFERENCES `personas` (`cedula`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `apartamentos_ibfk_2` FOREIGN KEY (`Inquilino`) REFERENCES `personas` (`cedula`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ingresos`
--
ALTER TABLE `ingresos`
  ADD CONSTRAINT `ingresos_ibfk_1` FOREIGN KEY (`nro_apartamento`) REFERENCES `apartamentos` (`nro_aparta`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `mensualidad`
--
ALTER TABLE `mensualidad`
  ADD CONSTRAINT `mensualidad_ibfk_1` FOREIGN KEY (`apartamento`) REFERENCES `apartamentos` (`nro_aparta`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
