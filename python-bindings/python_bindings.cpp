#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <iostream>
#include "../v1/src/burg_basic.hpp"

namespace py = pybind11;

PYBIND11_MODULE(burg_plc, m) {
    using data_type = double;
    py::class_<burg_basic<data_type>, std::shared_ptr<burg_basic<data_type>>> bec(m, "BurgBasic");

    bec.def(py::init<const std::size_t>())
       .def("fit", &burg_basic<data_type>::fit)
       .def("predict", &burg_basic<data_type>::predict);
    
    m.doc() = "C++ implementation of the Burg PLC algorithm";
}